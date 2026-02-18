# app/routes.py
from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app, jsonify
from app.services.aws_contact import save_contact_message, maybe_send_email

bp = Blueprint("site", __name__)

@bp.get("/")
def home():
    return render_template("home.html", active="home")

@bp.get("/who-we-are")
def who_we_are():
    return render_template("who_we_are.html", active="who")

@bp.get("/who-guides-us")
def who_guides_us():
    return render_template("who_guides_us.html", active="who")

@bp.get("/who-serves-you")
def who_serves_you():
    return render_template("who_serves_you.html", active="who")

@bp.get("/who-we-rockin-with")
def who_we_rockin_with():
    return render_template("who_we_rockin_with.html", active="who")

@bp.get("/how-we-support")
def how_we_support():
    return render_template("how_we_support.html", active="support")

@bp.get("/faqs")
def faqs():
    return render_template("faqs.html", active="faqs")

@bp.get("/get-started")
def get_started():
    return render_template("get_started.html", active="support")

@bp.get("/donate")
def donate():
    return render_template("donate.html", active="")

@bp.post("/contact")
def contact():
    name = (request.form.get("name") or "").strip()
    email = (request.form.get("email") or "").strip()
    message = (request.form.get("message") or "").strip()

    if not name or not email or not message:
        flash("Please fill out name, email, and message.", "error")
        return redirect(request.referrer or url_for("site.home"))

    try:
        if not current_app.config.get("DEV_MODE"):
            save_contact_message(
                region=current_app.config["AWS_REGION"],
                table_name=current_app.config["DDB_CONTACT_TABLE"],
                name=name,
                email=email,
                message=message,
                user_ip=request.headers.get("X-Forwarded-For", request.remote_addr),
                user_agent=request.headers.get("User-Agent"),
            )

            maybe_send_email(
                region=current_app.config["AWS_REGION"],
                from_email=current_app.config.get("SES_FROM_EMAIL", ""),
                to_email=current_app.config.get("SES_TO_EMAIL", ""),
                subject=f"New message from {name}",
                body=f"Name: {name}\nEmail: {email}\n\n{message}",
            )
    except Exception:
        # don't break UI in test deploys
        pass

    flash("Thanks for reaching out — we’ll get back to you soon.", "success")
    return redirect(request.referrer or url_for("site.home"))


@bp.post("/analytics")
def analytics():
    data = request.get_json(silent=True) or {}
    # For now, just print (later: DynamoDB/S3/CloudWatch)
    current_app.logger.info("ANALYTICS %s", data)
    return jsonify({"ok": True})

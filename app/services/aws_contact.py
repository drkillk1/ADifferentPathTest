# app/services/aws_contact.py
import uuid
from datetime import datetime, timezone
from typing import Optional
import boto3

def save_contact_message(*,
    region: str,
    table_name: str,
    name: str,
    email: str,
    message: str,
    user_ip: Optional[str],
    user_agent: Optional[str],
):
    ddb = boto3.resource("dynamodb", region_name=region)
    table = ddb.Table(table_name)

    now = datetime.now(timezone.utc).isoformat()
    item = {
        "pk": "CONTACT",
        "sk": f"{now}#{uuid.uuid4().hex}",
        "created_at": now,
        "name": name,
        "email": email,
        "message": message,
        "user_ip": user_ip or "",
        "user_agent": user_agent or "",
    }
    table.put_item(Item=item)

def maybe_send_email(*,
    region: str,
    from_email: str,
    to_email: str,
    subject: str,
    body: str,
):
    if not from_email or not to_email:
        return

    ses = boto3.client("ses", region_name=region)
    ses.send_email(
        Source=from_email,
        Destination={"ToAddresses": [to_email]},
        Message={
            "Subject": {"Data": subject},
            "Body": {"Text": {"Data": body}},
        },
    )

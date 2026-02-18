import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-change-me")

    # Dev flag
    DEV_MODE = os.getenv("DEV_MODE", "1") == "1"

    AWS_REGION = os.getenv("AWS_REGION", "us-west-1")
    DDB_CONTACT_TABLE = os.getenv("DDB_CONTACT_TABLE", "adp_contact_messages")

    SES_FROM_EMAIL = os.getenv("SES_FROM_EMAIL", "")
    SES_TO_EMAIL = os.getenv("SES_TO_EMAIL", "")

    GET_STARTED_URL = os.getenv("GET_STARTED_URL", "/get-started")
    VOLUNTEER_URL = os.getenv("VOLUNTEER_URL", "https://docs.google.com/forms/d/e/1FAIpQLScZUWTcv6eQp7S13FtIgNjR8F4v_GpAliyrfzWJ-Q5ed8cOhQ/viewform")
    INSTAGRAM_URL = os.getenv("INSTAGRAM_URL", "https://www.instagram.com/_adifferentpath/#")
    DONATE_URL = os.getenv("DONATE_URL", "/donate")

    FORM_FOOTPRINTS_URL = os.getenv("FORM_FOOTPRINTS_URL", "")
    FORM_COUNSELING_URL = os.getenv("FORM_COUNSELING_URL", "")
    FORM_LIFE_COACHING_URL = os.getenv("FORM_LIFE_COACHING_URL", "")
    FORM_ALT_SENTENCING_URL = os.getenv("FORM_ALT_SENTENCING_URL", "")
    FORM_COMMUNITY_PROGRAMS_URL = os.getenv("FORM_COMMUNITY_PROGRAMS_URL", "")
    FORM_PRO_DEV_URL = os.getenv("FORM_PRO_DEV_URL", "")
    FORM_GET_INVOLVED_URL = os.getenv("FORM_GET_INVOLVED_URL", "")

    

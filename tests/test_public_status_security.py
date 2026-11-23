from pathlib import Path


def test_public_status_page_never_embeds_admin_credentials_or_calls_private_routes():
    status_page = Path(__file__).resolve().parents[1] / "status.html"
    source = status_page.read_text(encoding="utf-8")

    forbidden = (
        "ADMIN_KEY",
        "ADMIN_API_KEY",
        "admin_secret_key_change_me_2026",
        "/admin/",
    )
    for value in forbidden:
        assert value not in source


def test_public_status_page_limits_checks_to_public_health_and_stripe_config():
    status_page = Path(__file__).resolve().parents[1] / "status.html"
    source = status_page.read_text(encoding="utf-8")

    assert "API + '/health'" in source
    assert "API + '/stripe/config'" in source
    assert "live verification pending" in source
    assert "Public API operational" in source

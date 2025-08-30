from datetime import datetime

def validate_date(date_str: str) -> bool:
    """Validate date in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str.strip(), "%Y-%m-%d")
        return True
    except Exception:
        return False

def validate_amount(amount_str: str) -> float | None:
    """Return a positive float if valid, else None."""
    try:
        val = float(amount_str)
        if val > 0:
            return val
        return None
    except Exception:
        return None

def validate_nonempty(s: str) -> bool:
    return bool(s and s.strip())

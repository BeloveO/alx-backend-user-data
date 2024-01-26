#!/usr/bin/env python3
"""
Authentication through hash password
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash the password
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

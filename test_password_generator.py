import pytest
import string
from password_generator import generate_secure_password

def test_password_length():
    lengths = [4, 8, 16, 32]
    for length in lengths:
        password = generate_secure_password(length)
        assert len(password) == length, f"Password length should be {length}"

def test_password_contains_all_types():
    password = generate_secure_password(32)
    assert any(c in string.ascii_lowercase for c in password), "Password should contain at least one lowercase letter"
    assert any(c in string.ascii_uppercase for c in password), "Password should contain at least one uppercase letter"
    assert any(c in string.digits for c in password), "Password should contain at least one digit"
    assert any(c in string.punctuation for c in password), "Password should contain at least one punctuation character"

def test_password_randomness():
    # Generate a set of 1 million passwords and check their uniqueness
    passwords = {generate_secure_password(32) for _ in range(1000000)}
    assert len(passwords) == 1000000, "Generated passwords should be unique"

def test_invalid_length():
    with pytest.raises(ValueError, match="La longitud de la contraseña debe ser al menos 4 para incluir todos los tipos de caracteres."):
        generate_secure_password(3)

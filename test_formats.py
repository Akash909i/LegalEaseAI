from backend.document_formats import (
    as_txt,
    as_docx,
    as_pdf,
)


def test_txt():

    result = as_txt(
        "Hello LegalEase"
    )

    assert result.startswith(
        b"Hello"
    )


def test_docx():

    result = as_docx(
        text="HELLO\n1. TEST",
        title="NDA",
        terms=(
            "Confidentiality; Payment"
        ),
    )

    # DOCX files are ZIP containers
    assert result[:2] == b"PK"


def test_pdf():

    result = as_pdf(
        text="HELLO\n1. TEST",
        title="NDA",
    )

    assert result.startswith(
        b"%PDF"
    )
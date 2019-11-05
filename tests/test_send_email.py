import pytest

from settings import MENSAGEM_1, MENSAGEM_2


def test_send_email(mocker):
    smtp = mocker.patch("smtplib.SMTP")
    import send_email
    smtp().sendmail.call_count == 3
    len(smtp().sendmail.call_args_list) == 3

import smtplib
import random
import math

class OTPService:
    @staticmethod
    def enviar_otp_email(destinatario):
        n = "0123456789"
        otp = ""
        for i in range(6):
            otp += n[math.floor(random.random() * 10)]

        message = f"{otp} is your One-Time-Password for verification"

        email = smtplib.SMTP(host='smtp.gmail.com', port=587)
        email.starttls()

        # Aqui é necessário conectar uma conta Gmail seguindo os passos em:
        # https://support.google.com/mail/answer/185833?hl=en#
        email.login(user="codingtestscamilavieira@gmail.com", password="czsc zwfm qolp iwbn")

        email.sendmail(from_addr="codingtestscamilavieira@gmail.com", to_addrs=destinatario, msg=message)

        print("OTP enviado com sucesso para o e-mail fornecido.")

        email.quit()

        return otp  # Retorna o OTP gerado para ser verificado posteriormente

    @staticmethod
    def verificar_otp(otp_digitado, otp_gerado):
        return otp_digitado == otp_gerado

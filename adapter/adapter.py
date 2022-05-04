class _Telefone:
    def telefonar(self, ddd, numero):
        print(f"ligando para ({ddd}{numero})")


class _WhatsappApi:
    def call(self, phone):
        """phone must be on format +country code and phone number"""
        print(f'zap zap call to whatsapp from {phone}')


class WhatsappApiToTelefoneAdapter:
    def __init__(self, whatsapp_api):
        self.whatsapp_api = whatsapp_api

    def telefonar(self, ddd, telefone):
        return self.whatsapp_api.call(f'+55{ddd}{telefone}')


class _TelegramApiEspn:
    def llamar(self, country_code, phone):
        """phone must be on format +country code and phone number"""
        print(f"called to telegram from {country_code} {phone}")


class TelegramParaTelefoneAdapterMixin:
    def telefonar(self, ddd, telefone):
        self.llamar('+55', f'{ddd}{telefone}')


class TelegramParaTelefoneAdapter(TelegramParaTelefoneAdapterMixin, _TelegramApiEspn):
    pass


# telefone = _Telefone()
# telefone = WhatsappApiToTelefoneAdapter(_WhatsappApi())
telefone = TelegramParaTelefoneAdapter()


if __name__ == "__main__":
    telefone.telefonar('12', '23456789')
    telefone.telefonar('31', '88819529')

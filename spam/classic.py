from abc import ABC, abstractmethod


class SpamAbstrata(ABC):
    def enviar_spam_para_todos_usuarios(self, msg):
        # obter a lista contatos
        for nome, endereco in self.obter_contatos():
            # Para cada usuario, enviar uma msg pelo canal
            self.enviar_mensagem(nome, endereco, msg)

        @abstractmethod
        def obter_contatos(self):
            """deve retornar uma lista onde cada elemento é uma tupla \
                    O primeiro elemento nome, segundo endereco no respectivo \
                    canal"""

        @abstractmethod
        def enviar_ensagem(self, nome, endereco, msg):
            """deve enviar mensagem para usuario
            :param nome: str nome usuario
            :param endereco: str endereco usuario
            :param msg: str mensagem a ser enviada
            :return: booleano indicando se mensagem foi enviada ou não
            """


if __name__ == "__main__":

    class SpamParaConsole(SpamAbstrata):
        def obter_contatos(self):
            return [('ali', 'ali@email.com'), ('jonathan', 'jonathan@email.com')]

        def enviar_mensagem(self, nome, endereco, msg):
            print(f"Msg para  {nome} no endereco {endereco}: {msg}")

    spam_para_console = SpamParaConsole()

    spam_para_console.enviar_spam_para_todos_usuarios('Ola template method')

class Target:
    """
    the target defines the domain-specific interface used by the client \
            code.
    """
    def request(self) -> str:
        return "target: the default target's behavior."

class Adaptee:
    """
    the adaptee contains some useful behavior, but its interface \
            is incompatible with the existing client code. the adapter \
            needs some adaptation before the cliente code can use it.
    """

    def specific_request(self) -> str:
        return "special behavior the adaptee"


class Adapter(Target, Adaptee):
    """
    the adapter makes the adaptee's interface compatible with \
            the target's interface via multiple inheritance.
            """

    def request(self) -> str:
        return f"adapter: (translated) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    the client code supports all clases that follow the target interface.
    """
    print(target.request(), end="")


if __name__ == "__main__":
    print("client: I can work just fine with the target objets:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("client: the adaptee class has a weird interface."
            "see, i don't understant it:")
    print(f"adaptee: {adaptee.specific_request()}", end="\n\n")
    print("client: but i can work with it via the adapter.")
    adapter = print("client: but i can work with it via the adapter.")
    adapter = Adapter()
    client_code(adapter)

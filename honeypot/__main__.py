import sys


def main(argv: list[str]):
    if len(argv) == 2 and argv[1] == "client":
        import client
        client.start()
        return

    import server
    server.start()


if __name__ == "__main__":
    main(sys.argv)

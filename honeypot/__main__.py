from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("client", help="run the client")
    server_subparser = subparsers.add_parser("server", help="run the server")

    server_subparser.add_argument(
        "-c",
        "--packet-capture",
        action="store_true",
        help="run server with packet capture feature (run as Admin)"
    )

    server_subparser.add_argument(
        "-d",
        "--intrusion-detection",
        action="store_true",
        help="run server with intrusion detection feature (run as Admin)"
    )

    server_subparser.add_argument(
        "-a",
        "--all-features",
        action="store_true",
        help="run server with all features (run as Admin)"
    )

    args = parser.parse_args()
    args_dictionary = vars(args)

    if args_dictionary.pop("command") == "client":
        import client
        client.start()
        return

    import server
    server.start(**args_dictionary)


if __name__ == "__main__":
    main()

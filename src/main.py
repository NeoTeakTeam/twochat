import click as c
from rich import print


@c.group(name="Two Chat")
def cli():
    pass


def main():
    print("[blue]Two Chat[/blue]")
    print("[green]聊天新方式[/green]")
    print()

    cli()


if __name__ == "__main__":
    main()

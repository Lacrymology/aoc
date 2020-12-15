import argparse
import importlib


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Run ShipHero Shipping")

    parser.add_argument("day", help="Day to run. E.g.: day_1", type=str)
    parser.add_argument(
        "--event", help="Event to run from. E.g.: day_1", default="event2020", type=str
    )

    args = parser.parse_args()

    importlib.import_module(f"{args.event}.{args.day}")
import argparse

try:
    from .app import run_llamaindex_mission
except ImportError:
    from app import run_llamaindex_mission


def demo(mission: str) -> None:
    out = run_llamaindex_mission(mission)
    print("[LlamaIndex] primary:", out.get("primary"))
    print("[LlamaIndex] support:", out.get("support"))
    print("[LlamaIndex] result:", out.get("result"))
    print("[LlamaIndex] verification:", out.get("verification"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mission", default="research market and produce launch strategy")
    args = parser.parse_args()
    demo(args.mission)

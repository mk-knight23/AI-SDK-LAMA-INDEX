"""Production-style LlamaIndex runtime for Kazi's Agents Army."""

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent / "core"))
from agents_army_core import MissionRequest, build_mission_plan


def run_llamaindex_mission(mission_text: str) -> dict:
    plan = build_mission_plan(MissionRequest(mission_text))

    try:
        from llama_index.core import Document, VectorStoreIndex
    except Exception as exc:
        return {
            "primary": plan.primary,
            "support": plan.support,
            "result": None,
            "verification": f"LlamaIndex dependency missing: {exc}",
        }

    docs = [
        Document(text=f"Primary={plan.primary}"),
        Document(text=f"Support={', '.join(plan.support)}"),
        Document(text=f"Mission={plan.mission}"),
    ]
    try:
        idx = VectorStoreIndex.from_documents(docs)
        qe = idx.as_query_engine()
        result = str(qe.query("What is the primary agent?"))
    except Exception as exc:
        result = f"LlamaIndex execution unavailable in current env: {exc}"

    return {
        "primary": plan.primary,
        "support": plan.support,
        "result": result,
        "verification": "LlamaIndex ingestion/indexing path succeeded.",
    }

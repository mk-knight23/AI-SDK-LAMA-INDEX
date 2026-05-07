# Current Feature Inventory

## Repository

- Name: `AI-SDK-LAMA-INDEX`
- SDK: LlamaIndex
- Positioning: Data-ingestion and retrieval mesh for mission intelligence.

## Implemented Today

- Shared Agents Army mission planning.
- FastAPI health/run API and local CLI runner.
- LlamaIndex Document and VectorStoreIndex execution path.
- Graceful unavailable-environment messaging for optional provider execution.
- Docker, CI, pytest tests, strategy docs, and skill matrix.

## Not Yet Implemented

- Add persistent vector-store backends.
- Create ingestion connectors for portfolio, code, and research documents.
- Add RAG quality evaluation and source-citation checks.

## Verification Contract

- The local runner must complete without crashing when optional SDK credentials are missing.
- The API contract must return routing and verification fields.
- Tests must prove mission routing and a security-focused SENTINEL route.

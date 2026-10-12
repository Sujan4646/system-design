# System Design Interview Cheat Sheet

## 1. 4-Step Interview Framework (45 Minutes)

| Time | Phase | Focus |
|---|---|---|
| **0-5 min** | **Requirements & Scope** | Functional requirements, Non-functional (availability, latency, consistency), Constraints (DAU, RPS, storage). |
| **5-15 min** | **High-Level Design** | API endpoints, high-level diagram, database schema, data flow. |
| **15-35 min** | **Deep Dive** | Bottlenecks, caching, database partitioning, data replication, load balancing, message queues. |
| **35-45 min** | **Wrap Up & Trade-offs** | Single point of failure (SPOF), monitoring, failure handling, scale-out limits. |

---

## 2. Rule-of-Thumb Estimations
- 1 day = 86,400 seconds $\approx 10^5$ seconds.
- Requests per second (RPS) = `Total Requests per Day / 86,400`.
- Peak RPS = `Average RPS * 2` (or 3 depending on domain).
- 1 KB = $10^3$ bytes, 1 MB = $10^6$ bytes, 1 GB = $10^9$ bytes, 1 TB = $10^{12}$ bytes, 1 PB = $10^{15}$ bytes.

---

## 3. Storage Technology Decision Matrix

| Requirement | Preferred Database |
|---|---|
| ACID transactions, complex joins, structured tabular data | PostgreSQL, MySQL |
| High-throughput writes, time-series, wide-column | Cassandra, ScyllaDB |
| Document storage, flexible schemas, rapid prototyping | MongoDB, Couchbase |
| Ultra low latency key-value reads/writes | Redis, DynamoDB |
| Full-text search and inverted index queries | Elasticsearch, OpenSearch |
| Highly interconnected graph relations (social graphs, fraud detection) | Neo4j, Amazon Neptune |

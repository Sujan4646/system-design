# CAP Theorem & PACELC

The **CAP Theorem** states that any distributed data store can only guarantee at most two of the following three properties simultaneously:

1. **Consistency (C)**: Every read receives the most recent write or an error.
2. **Availability (A)**: Every non-failing node returns a non-error response for every request (without guarantee that it contains the most recent write).
3. **Partition Tolerance (P)**: The system continues to operate despite arbitrary network partitions (packet drops or delays between nodes).

Because network partitions ($P$) cannot be avoided in real distributed networks, systems must choose between:
- **CP (Consistency + Partition Tolerance)**: Sacrifice availability when partitions happen (e.g., return errors/timeout to preserve strict consistency). Examples: HBase, BigTable, ZooKeeper, CockroachDB.
- **AP (Availability + Partition Tolerance)**: Return potentially stale data during partitions to maintain availability. Examples: Cassandra, DynamoDB, CouchDB.

---

## Beyond CAP: PACELC Theorem

In 2012, Daniel Abadi expanded CAP into **PACELC**:

> **If there is a Partition (P):**
> How does the system trade off **Availability (A)** and **Consistency (C)**?
>
> **Else (E - normal operation):**
> How does the system trade off **Latency (L)** and **Consistency (C)**?

### PACELC Classifications:
| System | PACELC Category | Behavior |
|---|---|---|
| **DynamoDB / Cassandra** | **PA/EL** | High availability during partitions, low latency during normal operations (eventual consistency). |
| **MongoDB** | **PC/EC** | Consistent on partition; consistent over latency during normal operations. |
| **Spanner / CockroachDB** | **PC/EC** | Prioritizes strong serializable consistency always. |

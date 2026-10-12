# Database Sharding & Partitioning

Sharding is the process of horizontally partitioning a database into smaller, faster, and more easily managed pieces called shards.

---

## 1. Sharding Strategies

### A. Range-Based Sharding
- Split data according to continuous ranges of a key (e.g., User IDs 1-1M -> Shard 1, 1M-2M -> Shard 2).
- **Pros**: Easy to implement; range queries are efficient on a single shard.
- **Cons**: High risk of hotspotting (e.g., recent dates or active IDs overburdening a single shard).

### B. Hash-Based Sharding
- Compute `hash(shard_key) % N` where $N$ is the number of shards.
- **Pros**: Uniform distribution of data and traffic.
- **Cons**: Adding/removing shards requires massive rehashing unless consistent hashing is used.

### C. Consistent Hashing
- Nodes and keys are mapped along a virtual 360-degree hash ring.
- Adding or removing a node only impacts keys between adjacent nodes ($K/N$ keys on average).
- Virtual nodes (vnodes) prevent skewed distributions.

---

## 2. Common Challenges with Sharding
- **Cross-shard joins**: Very expensive or unsupported; requires denormalization.
- **Distributed transactions**: Requires two-phase commit (2PC) or Saga patterns, increasing latency.
- **Resharding**: Rebalancing shards when data grows unevenly requires complex online migration.

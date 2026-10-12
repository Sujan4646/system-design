# Load Balancing

Load balancers distribute incoming network traffic across a cluster of servers to improve responsiveness, availability, and resilience.

---

## 1. OSI Layer Load Balancing

### Layer 4 (Transport Layer)
- Routes traffic based on IP address and TCP/UDP port without inspecting application payload.
- Extremely high throughput and low overhead.
- Examples: AWS NLB, IPVS, HAProxy (TCP mode).

### Layer 7 (Application Layer)
- Inspects HTTP/HTTPS headers, cookies, URL paths, and request payloads.
- Enables path-based routing (e.g., `/api/v1/auth` vs `/api/v1/billing`), SSL termination, and cookie affinity.
- Examples: NGINX, AWS ALB, Envoy, Traefik.

---

## 2. Load Balancing Algorithms

| Algorithm | Mechanism | Best Use Case |
|---|---|---|
| **Round Robin** | Sequentially sends requests to each server in order. | Homogeneous servers and requests with uniform compute costs. |
| **Least Connections** | Directs traffic to the server currently handling the fewest active connections. | Long-lived connections (WebSockets, database sessions). |
| **Weighted Round Robin** | Allocates higher proportions of traffic to higher-capacity servers. | Heterogeneous server clusters. |
| **IP Hash** | Computes hash of client IP to map client consistently to the same server. | Stateful sessions without shared distributed cache. |
| **Least Response Time** | Routes to server with lowest latency and fewest connections. | Dynamic response-time sensitive services. |

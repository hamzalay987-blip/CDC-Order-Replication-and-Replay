# Project notes: CDC Order Replication and Replay

**Business problem:** Downstream consumers need correct state when change events are duplicated, reordered, or replayed.

**Design:** Maintain per-key event sequence numbers and apply only newer events, including tombstones.

**Interview discussion:** Explain schema assumptions, late data/duplicate behavior, controls, expected tradeoffs, and what would change at enterprise scale.

**Suggested next feature:** Add sample-sized integration tests or a docker-compose service when the implementation is ready.

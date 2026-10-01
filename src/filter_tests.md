
# Firewall Filter Tests

## Laboratory Environment

The firewall tests were designed for an authorised laboratory environment.

| Component | Address / Service |
|---|---|
| Student Records Server | 192.168.10.10 |
| Guest Network | 192.168.20.0/24 |
| Authorised Staff Network | 192.168.30.0/24 |
| Protected Service | SSH |
| Protocol | TCP |
| Port | 22 |

---

## Test 1 – Authorised Staff Access

### Purpose

Verify that an authorised staff computer can access the protected SSH service.

### Command

```bash
nc -vz 192.168.10.10 22
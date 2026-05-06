## Intentional Security Validation

To verify that the security controls actually work, I intentionally tested controlled insecure examples:

| Test | Tool | Expected result | Outcome |
|---|---|---|---|
| Fake secret committed to repository | Gitleaks | Pipeline fails | Passed |
| Static code analysis | Semgrep | Finding reported in CI | Passed |
| Vulnerable container/dependencies | Trivy | Pipeline fails on HIGH/CRITICAL findings | Passed |

These tests helped validate that the pipeline detects risky changes before they are merged.
##Pipeline stage: CI tests##

Purpose:
Validate that the application works before running security checks.

Trigger:
Pull request and push.

Failure condition:
Tests fail.

##pipeline stage: Docker build##
Purpose:
Verify that the application can be built into a container image.

Why it matters:
If the Docker image cannot be built, it should not move to security scanning or deployment.


##Control: Secret scanning##
Tool:
Gitleaks
Risk addressed:
Accidental commit of API keys, passwords or tokens.
Test:
I intentionally added a fake secret pattern to verify that the pipeline detects it.
Result:
The pipeline failed as expected.
Remediation:
The fake secret was removed and the pipeline passed.

Control: Static application security testing

Tool:
Semgrep / CodeQL

Risk addressed:
Insecure coding patterns detected before push to production.

Where it runs:
Push request pipeline.
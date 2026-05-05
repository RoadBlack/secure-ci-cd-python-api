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

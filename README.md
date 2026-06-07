# Shinsekai CI Smoke Plugin

This repository is a tiny Shinsekai plugin used to verify the plugin distribution pipeline.

It is intentionally small, but it covers the release flow:

- Registry Issue submission with basic metadata.
- CI inference from a root-level `plugin.py`.
- Version inference from `plugin_version`.
- Logo discovery from `logo.png`.
- R2 package build and client installation.
- Dependency installation from `requirements.txt`.

## Plugin Metadata

- Display name: Shinsekai CI Smoke
- Plugin id: `com.shinsekai.ci_smoke`
- Minimum Shinsekai version: `>=0.2.0`
- Repository: `https://github.com/End0rph1nww/shinsekai-plugin-ci-smoke`

## Expected Entry

Registry CI should infer this entry:

```text
plugins.shinsekai_plugin_ci_smoke.plugin:ShinsekaiCiSmokePlugin
```

## Manual Local Install

After downloading this repository under Shinsekai `plugins/`, add this manifest entry if needed:

```yaml
- entry: plugins.shinsekai_plugin_ci_smoke.plugin:ShinsekaiCiSmokePlugin
  enabled: true
```


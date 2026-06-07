from __future__ import annotations

from pathlib import Path

from sdk.plugin import PluginBase
from sdk.plugin_host_context import PluginHostContext
from sdk.register import PluginCapabilityRegistry


class ShinsekaiCiSmokePlugin(PluginBase):
    """Minimal plugin used to verify Registry and R2 distribution."""

    @property
    def plugin_id(self) -> str:
        return "com.shinsekai.ci_smoke"

    @property
    def plugin_version(self) -> str:
        return "0.1.1"

    @property
    def plugin_name(self) -> str:
        return "Shinsekai CI Smoke"

    @property
    def plugin_description(self) -> str:
        return "Small test plugin for Registry Issue, R2 package, logo and update detection flows."

    @property
    def plugin_author(self) -> str:
        return "Shinsekai Contributors"

    def initialize(
        self,
        register: PluginCapabilityRegistry,
        plugin_root: Path,
        host: PluginHostContext,
    ) -> None:
        _ = register, plugin_root, host

        # Imported during initialization so dependency installation is exercised by smoke tests.
        import colorama  # noqa: F401

    def shutdown(self) -> None:
        return None


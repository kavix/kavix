
<sub>*Prior work as [kavindus0](https://github.com/kavindus0) is archived.*</sub>
---
<details>
<summary><h3>Open Source Contributions</h3></summary>

<br>

#### Cloud Native & Kubernetes

<details>
<summary><strong><a href="https://github.com/GoogleContainerTools/skaffold">GoogleContainerTools/skaffold</a></strong></summary>

- [fix(filter): guard kyaml pass to prevent dropping trailing newlines](https://github.com/GoogleContainerTools/skaffold/pull/10166)

</details>

<details>
<summary><strong><a href="https://github.com/kgateway-dev/kgateway">kgateway-dev/kgateway</a></strong></summary>

- [feat: Add secretRefs to TrafficPolicy transformations (fixes #14594)](https://github.com/kgateway-dev/kgateway/pull/14629)

</details>

<details>
<summary><strong><a href="https://github.com/kubernetes-sigs/cloud-provider-azure">kubernetes-sigs/cloud-provider-azure</a></strong></summary>

- [Feat: Fault domain behavior enhancement](https://github.com/kubernetes-sigs/cloud-provider-azure/pull/10907)
- [Fix case-insensitive duplicate tags](https://github.com/kubernetes-sigs/cloud-provider-azure/pull/10906)

</details>

<details>
<summary><strong><a href="https://github.com/kubernetes-sigs/inference-perf">kubernetes-sigs/inference-perf</a></strong></summary>

- [Fix issue 732: circuit breaker edge cases and tests](https://github.com/kubernetes-sigs/inference-perf/pull/766)

</details>

<details>
<summary><strong><a href="https://github.com/kubernetes-sigs/kueue">kubernetes-sigs/kueue</a></strong></summary>

- [[release-0.19] WAS: Discard logs in simulator context to avoid race during teardown](https://github.com/kubernetes-sigs/kueue/pull/14913)
- [queue: use cmp.Or for requeueWorkload nil fallback in manager_test.go](https://github.com/kubernetes-sigs/kueue/pull/14912)
- [WAS: Discard logs in simulator context to avoid race during teardown](https://github.com/kubernetes-sigs/kueue/pull/14908)
- [integration: Bound MultiKueue manager shutdown during teardown](https://github.com/kubernetes-sigs/kueue/pull/14904)
- [test: add scale-down coverage for elastic job ungater](https://github.com/kubernetes-sigs/kueue/pull/14897)
- [Wrap pending workloads bucket operations in helpers to keep scheduling hashes in sync](https://github.com/kubernetes-sigs/kueue/pull/14889)
- [Preserve unmodeled spec fields when MultiKueue SyncJob creates remote jobs](https://github.com/kubernetes-sigs/kueue/pull/14849)
- [metrics: correct comment on RecordPodSchedulingGateRemovalSeconds](https://github.com/kubernetes-sigs/kueue/pull/14740)
- [Propagate wlName to reconcileWorkload in StatefulSet reconciler](https://github.com/kubernetes-sigs/kueue/pull/14721)
- [test(pod): Add unit tests for IndexPodGroupName](https://github.com/kubernetes-sigs/kueue/pull/14718)
- [Assert nil admission warnings in webhook validation tests](https://github.com/kubernetes-sigs/kueue/pull/14715)
- [Consolidate StatefulSet Pod defaulting reconciliation](https://github.com/kubernetes-sigs/kueue/pull/14597)
- [docs: keep importer flag list in alphabetical order](https://github.com/kubernetes-sigs/kueue/pull/14593)
- [Ensure simulator and TAS snapshots share node state](https://github.com/kubernetes-sigs/kueue/pull/14560)
- [feat: make workloads popped per ClusterQueue configurable](https://github.com/kubernetes-sigs/kueue/pull/14553)
- [Remove unused resource.IsZero function](https://github.com/kubernetes-sigs/kueue/pull/14546)

</details>

<details>
<summary><strong><a href="https://github.com/ray-project/kuberay">ray-project/kuberay</a></strong></summary>

- [ray-operator: remove ineffective clearing of WorkersToDelete](https://github.com/ray-project/kuberay/pull/5209)

</details>

#### Developer Platforms & IDP

<details>
<summary><strong><a href="https://github.com/guidewire-oss/teams360">guidewire-oss/teams360</a></strong></summary>

- [Fix/branding rename pr 137](https://github.com/guidewire-oss/teams360/pull/141)
- [Kavix patch 1](https://github.com/guidewire-oss/teams360/pull/138)
- [docs(branding): rename Team360 to Team Health Check](https://github.com/guidewire-oss/teams360/pull/137)

</details>

<details>
<summary><strong><a href="https://github.com/openchoreo/backstage-plugins">openchoreo/backstage-plugins</a></strong></summary>

- [fix(permission-policy): preserve scoped capability paths for catalog entity visibility](https://github.com/openchoreo/backstage-plugins/pull/767)
- [feat: add SonarQube integration to entity pages](https://github.com/openchoreo/backstage-plugins/pull/662)
- [feat(observability): make project-level log component names clickable](https://github.com/openchoreo/backstage-plugins/pull/643)

</details>

<details>
<summary><strong><a href="https://github.com/openchoreo/openchoreo">openchoreo/openchoreo</a></strong></summary>

- [feat(api): support per-trigger cronjob arguments](https://github.com/openchoreo/openchoreo/pull/4577)
- [fix(controller): clean up orphaned ProjectRelease snapshots on Project deletion](https://github.com/openchoreo/openchoreo/pull/4406)
- [fix(controller): add container ports so workloads can be targeted by name](https://github.com/openchoreo/openchoreo/pull/4382)
- [feat(cli): add resource to occ config context scope](https://github.com/openchoreo/openchoreo/pull/4145)
- [feat(helm): enable WebSocket upgrades by default on KGateway](https://github.com/openchoreo/openchoreo/pull/4080)
- [fix(helm): gate KGateway TrafficPolicies on gatewayClassName](https://github.com/openchoreo/openchoreo/pull/4079)
- [feat(helm): enable WebSocket upgrades by default on KGateway](https://github.com/openchoreo/openchoreo/pull/4078)
- [feat(helm): enable WebSocket upgrades by default on KGateway](https://github.com/openchoreo/openchoreo/pull/4076)
- [feat(helm): enable WebSocket upgrades by default on KGateway](https://github.com/openchoreo/openchoreo/pull/4075)
- [Rename ReleaseBinding to ComponentReleaseBinding](https://github.com/openchoreo/openchoreo/pull/4072)
- [fix(controller): cascade Resource deletions and surface precise finalize statuses](https://github.com/openchoreo/openchoreo/pull/3917)
- [feat(helm): make gatewayClassName configurable in control and observability planes](https://github.com/openchoreo/openchoreo/pull/3915)
- [fix(controller): set workflow failed condition on validation failure](https://github.com/openchoreo/openchoreo/pull/3877)

</details>

<details>
<summary><strong><a href="https://github.com/openchoreo/openchoreo.github.io">openchoreo/openchoreo.github.io</a></strong></summary>

- [docs: add migration note for default-httplistenerpolicy Helm ownership conflict](https://github.com/openchoreo/openchoreo.github.io/pull/751)

</details>

<details>
<summary><strong><a href="https://github.com/openchoreo/sample-gitops">openchoreo/sample-gitops</a></strong></summary>

- [refactor(doclet): migrate postgres and nats components to resources](https://github.com/openchoreo/sample-gitops/pull/46)

</details>

#### Identity, Access Management & Security

<details>
<summary><strong><a href="https://github.com/Hushield/hushield">Hushield/hushield</a></strong></summary>

- [ci added](https://github.com/Hushield/hushield/pull/12)

</details>

<details>
<summary><strong><a href="https://github.com/asgardeo/javascript">asgardeo/javascript</a></strong></summary>

- [refactor: remove __legacy__ folders from packages](https://github.com/asgardeo/javascript/pull/539)

</details>

<details>
<summary><strong><a href="https://github.com/smallstep/cli">smallstep/cli</a></strong></summary>

- [Add --confirm flag to require agent confirmation](https://github.com/smallstep/cli/pull/1654)

</details>

<details>
<summary><strong><a href="https://github.com/thunder-id/thunderid">thunder-id/thunderid</a></strong></summary>

- [Add responsive markdown table renderer](https://github.com/thunder-id/thunderid/pull/5030)
- [docs(frontend): evaluate oxlint as potential ESLint replacement](https://github.com/thunder-id/thunderid/pull/4672)
- [Centralize OTP generation attempt validation into core OTP service](https://github.com/thunder-id/thunderid/pull/4334)
- [Improve docs home mobile responsiveness](https://github.com/thunder-id/thunderid/pull/3962)
- [Standardize context variable resolution pattern in HttpRequestExecutor](https://github.com/thunder-id/thunderid/pull/3636)
- [Return specific error for attribute conflicts during user provisioning](https://github.com/thunder-id/thunderid/pull/3317)
- [Use camelCase for declarative resource attributes](https://github.com/thunder-id/thunderid/pull/3304)
- [Implement modularized workflow validation and update build scripts](https://github.com/thunder-id/thunderid/pull/3172)

</details>

<details>
<summary><strong><a href="https://github.com/wso2/azure-terraform-modules">wso2/azure-terraform-modules</a></strong></summary>

- [Fix typo in variable name `nat_rule_name_shortned`](https://github.com/wso2/azure-terraform-modules/pull/212)

</details>

<details>
<summary><strong><a href="https://github.com/wso2/carbon-identity-framework">wso2/carbon-identity-framework</a></strong></summary>

- [Fix #28038: Reject multiple Authorization headers with 400 Bad Request](https://github.com/wso2/carbon-identity-framework/pull/8164)

</details>

<details>
<summary><strong><a href="https://github.com/wso2/healthcare-accelerator">wso2/healthcare-accelerator</a></strong></summary>

- [Fixes #21: Apply HTML attribute encoding to user inputs in JSP pages](https://github.com/wso2/healthcare-accelerator/pull/47)

</details>

<details>
<summary><strong><a href="https://github.com/wso2/product-is">wso2/product-is</a></strong></summary>

- [Add integration test for multiple Authorization headers rejection](https://github.com/wso2/product-is/pull/28058)
- [Introduce Session Data Optimizer v2 to optimize session data footprint](https://github.com/wso2/product-is/pull/28039)

</details>

#### Compilers, Runtimes & Languages

<details>
<summary><strong><a href="https://github.com/apple/container">apple/container</a></strong></summary>

- [perf(machine): fetch machines and default status concurrently in machine list](https://github.com/apple/container/pull/2214)
- [Add `cp` support to `container machine`](https://github.com/apple/container/pull/2211)

</details>

<details>
<summary><strong><a href="https://github.com/ballerina-platform/ballerina-lang">ballerina-platform/ballerina-lang</a></strong></summary>

- [Fix error propagation in lax optional field access](https://github.com/ballerina-platform/ballerina-lang/pull/44693)
- [Fix issue #22100: Improve error message for non-accessible object initialization](https://github.com/ballerina-platform/ballerina-lang/pull/44642)
- [Add --silent option to 'bal run' command](https://github.com/ballerina-platform/ballerina-lang/pull/44627)

</details>

<details>
<summary><strong><a href="https://github.com/ballerina-platform/module-ballerina-http">ballerina-platform/module-ballerina-http</a></strong></summary>

- [Support standard HTTP_PROXY, HTTPS_PROXY, and NO_PROXY environment variables](https://github.com/ballerina-platform/module-ballerina-http/pull/2631)

</details>

<details>
<summary><strong><a href="https://github.com/crate-ci/cargo-release">crate-ci/cargo-release</a></strong></summary>

- [feat: generate feature flag documentation](https://github.com/crate-ci/cargo-release/pull/987)

</details>

<details>
<summary><strong><a href="https://github.com/facebook/pyrefly">facebook/pyrefly</a></strong></summary>

- [Report redundant-condition for class instances without __bool__ or __len__](https://github.com/facebook/pyrefly/pull/4673)
- [Consider __all__.remove when determining explicit exports](https://github.com/facebook/pyrefly/pull/4638)
- [Fix stack overflow during subscript inference on recursive type aliases](https://github.com/facebook/pyrefly/pull/4635)
- [Guard against recursive protocol member checking in __getattr__ self validation](https://github.com/facebook/pyrefly/pull/4634)
- [Fix stack overflow from recursive Self __call__ resolution](https://github.com/facebook/pyrefly/pull/4591)
- [Fix deprecation warnings for re-exported symbols](https://github.com/facebook/pyrefly/pull/4577)
- [Support semantic tokens for format specifiers in logging calls](https://github.com/facebook/pyrefly/pull/4003)
- [Support multiple glob patterns in sub-config matches](https://github.com/facebook/pyrefly/pull/3516)

</details>

<details>
<summary><strong><a href="https://github.com/facebookresearch/projectaria_tools">facebookresearch/projectaria_tools</a></strong></summary>

- [Fix sample data paths to use gen1/mps_sample in Gen1 samples](https://github.com/facebookresearch/projectaria_tools/pull/396)
- [Fix apt install command for ADB in Linux USB driver docs](https://github.com/facebookresearch/projectaria_tools/pull/395)

</details>

<details>
<summary><strong><a href="https://github.com/modular/modular">modular/modular</a></strong></summary>

- [[Docs] Add license specification and README for max Mojo package (#6944)](https://github.com/modular/modular/pull/6950)
- [[mojo] Expose --check mode on mojo format](https://github.com/modular/modular/pull/6888)
- [[docs] Fix broken GPU programming tutorial link](https://github.com/modular/modular/pull/6882)

</details>

<details>
<summary><strong><a href="https://github.com/wso2/mi-vscode">wso2/mi-vscode</a></strong></summary>

- [Fix false-positive UndefinedVariable warning for foreach counter-variable](https://github.com/wso2/mi-vscode/pull/1523)

</details>

#### Other Open Source Contributions

<details>
<summary><strong><a href="https://github.com/LDFLK/OpenGIN">LDFLK/OpenGIN</a></strong></summary>

- [fix: make startup tests and database cleanup conditional](https://github.com/LDFLK/OpenGIN/pull/496)

</details>

<details>
<summary><strong><a href="https://github.com/LDFLK/openginxplore">LDFLK/openginxplore</a></strong></summary>

- [fix: add fallback for missing minister names in MinistryCard](https://github.com/LDFLK/openginxplore/pull/208)
- [GH-160: fix: add a way to exit the search results view](https://github.com/LDFLK/openginxplore/pull/207)

</details>

<details>
<summary><strong><a href="https://github.com/Termix-SSH/Termix">Termix-SSH/Termix</a></strong></summary>

- [Fix shared snippet folder visibility](https://github.com/Termix-SSH/Termix/pull/981)
- [Fix shared snippet folder visibility](https://github.com/Termix-SSH/Termix/pull/980)
- [Fix SSH port connection bug](https://github.com/Termix-SSH/Termix/pull/975)

</details>

<details>
<summary><strong><a href="https://github.com/clencyc/LiveEdit">clencyc/LiveEdit</a></strong></summary>

- [docs: add contributing guidelines and github templates](https://github.com/clencyc/LiveEdit/pull/20)

</details>

<details>
<summary><strong><a href="https://github.com/lingdojo/kana-dojo">lingdojo/kana-dojo</a></strong></summary>

- [content: add new japan fact](https://github.com/lingdojo/kana-dojo/pull/20437)
- [content: add video game quote](https://github.com/lingdojo/kana-dojo/pull/20436)

</details>

<details>
<summary><strong><a href="https://github.com/niro1-1/notebook-utils">niro1-1/notebook-utils</a></strong></summary>

- [feat: implement rate limiting and unit tests for failure scenarios (#32)](https://github.com/niro1-1/notebook-utils/pull/67)

</details>

</details>

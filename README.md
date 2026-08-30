# Hi there, I'm Kavindu 👋

> Systems, Cloud-Native, and Platform Engineer passionate about distributed systems, Kubernetes schedulers, developer tooling, and identity security.

### 🌐 Open Source Contributions

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

#### Developer Platforms & Tooling

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

#### Identity, Access & Security

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
<summary><strong><a href="https://github.com/BlackBossX/BusTicketGeneratingSystem">BlackBossX/BusTicketGeneratingSystem</a></strong></summary>

- [editByKavindus](https://github.com/BlackBossX/BusTicketGeneratingSystem/pull/6)

</details>

<details>
<summary><strong><a href="https://github.com/BlackBossX/elektrum-backend">BlackBossX/elektrum-backend</a></strong></summary>

- [CD](https://github.com/BlackBossX/elektrum-backend/pull/6)

</details>

<details>
<summary><strong><a href="https://github.com/Exp-Intro-to-GitHub-Flow-Cohort-2/series-intro-to-github-flow-kavindus0">Exp-Intro-to-GitHub-Flow-Cohort-2/series-intro-to-github-flow-kavindus0</a></strong></summary>

- [My first branch](https://github.com/Exp-Intro-to-GitHub-Flow-Cohort-2/series-intro-to-github-flow-kavindus0/pull/1)

</details>

<details>
<summary><strong><a href="https://github.com/ImKavinduSandaruwan/PyToolbox">ImKavinduSandaruwan/PyToolbox</a></strong></summary>

- [add dark/light mode toggle with enhanced styling](https://github.com/ImKavinduSandaruwan/PyToolbox/pull/1)

</details>

<details>
<summary><strong><a href="https://github.com/KODEGAS/.github">KODEGAS/.github</a></strong></summary>

- [Create README.md](https://github.com/KODEGAS/.github/pull/2)
- [Create README.md](https://github.com/KODEGAS/.github/pull/1)

</details>

<details>
<summary><strong><a href="https://github.com/KODEGAS/CareerCoachX">KODEGAS/CareerCoachX</a></strong></summary>

- [Aug 22 testing](https://github.com/KODEGAS/CareerCoachX/pull/1)

</details>

<details>
<summary><strong><a href="https://github.com/KODEGAS/KODEGAS-PADDY-API">KODEGAS/KODEGAS-PADDY-API</a></strong></summary>

- [[WIP] forcely set production url from 'https://kodegas-paddy-api.centralindia.cloudapp.azure.com' to 'http://kodegas-paddy-api.centralindia.cloudapp.azure.com](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/20)
- [[WIP] set production url from 'https://kodegas-paddy-api.centralindia.cloudapp.azure.com' to 'http://kodegas-paddy-api.centralindia.cloudapp.azure.com'](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/19)
- [Aug17](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/18)
- [Add favicon and improve medicine CRUD UI/logic](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/17)
- [Allow all origins in CORS configuration](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/16)
- [Refactor API key header handling in auth.py](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/15)
- [Update API base URLs to production server](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/14)
- [Reset file pointer before image processing](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/13)
- [Update CORS origins and prediction logic](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/12)
- [Create docker-image.yml](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/11)
- [Main meka sira main](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/10)
- [Main meka sira main](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/9)
- [Update auth.py](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/8)
- [Update root endpoint and CORS origins](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/7)
- [Add GitHub Actions deploy workflow and improve Dockerfile](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/6)
- [Create deploy.yml](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/5)
- [Kelauna eka](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/4)
- [Update openapi.json](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/3)
- [Update requirements.txt](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/2)
- [Update main.py](https://github.com/KODEGAS/KODEGAS-PADDY-API/pull/1)

</details>

<details>
<summary><strong><a href="https://github.com/KODEGAS/Medusa-2.0">KODEGAS/Medusa-2.0</a></strong></summary>

- [fix: Fix Docker and workflow issues for successful deployment](https://github.com/KODEGAS/Medusa-2.0/pull/26)
- [feat: Add backend deployment setup with Google Cloud and GHCR](https://github.com/KODEGAS/Medusa-2.0/pull/25)
- [Fix GitHub CI/CD: Resolve dependency conflicts, security vulnerabilities, and workflow issues](https://github.com/KODEGAS/Medusa-2.0/pull/23)
- [Fix GitHub Actions workflow YAML formatting issues](https://github.com/KODEGAS/Medusa-2.0/pull/22)
- [New brach](https://github.com/KODEGAS/Medusa-2.0/pull/9)
- [gh act](https://github.com/KODEGAS/Medusa-2.0/pull/8)
- [Reg moved](https://github.com/KODEGAS/Medusa-2.0/pull/7)
- [Reg moved](https://github.com/KODEGAS/Medusa-2.0/pull/6)
- [ci cd](https://github.com/KODEGAS/Medusa-2.0/pull/5)
- [gh ACT](https://github.com/KODEGAS/Medusa-2.0/pull/4)
- [static texts updated](https://github.com/KODEGAS/Medusa-2.0/pull/3)
- [/register moved](https://github.com/KODEGAS/Medusa-2.0/pull/2)

</details>

<details>
<summary><strong><a href="https://github.com/KODEGAS/vGurad_main">KODEGAS/vGurad_main</a></strong></summary>

- [Fix favicon implementation: Add missing favicon files and manifest.json](https://github.com/KODEGAS/vGurad_main/pull/19)
- [Fix GitHub Actions CI workflow failures - Node.js compatibility and dependency conflicts](https://github.com/KODEGAS/vGurad_main/pull/18)
- [Fix GitHub Actions CI workflow for monorepo structure and dependency conflicts](https://github.com/KODEGAS/vGurad_main/pull/17)
- [Update crop analysis API endpoint from HTTP to HTTPS](https://github.com/KODEGAS/vGurad_main/pull/16)
- [Document predict endpoints base URLs and configuration](https://github.com/KODEGAS/vGurad_main/pull/14)
- [Document and centralize API base URL configuration](https://github.com/KODEGAS/vGurad_main/pull/13)
- [Add i18n support to Admin and MarketPrices pages](https://github.com/KODEGAS/vGurad_main/pull/12)
- [Enhance SVG icon styling for priority medicine](https://github.com/KODEGAS/vGurad_main/pull/11)
- [Update .gitignore and frontend stats, fix formatting](https://github.com/KODEGAS/vGurad_main/pull/10)
- [Update .gitignore](https://github.com/KODEGAS/vGurad_main/pull/9)
- [Create node.js.yml](https://github.com/KODEGAS/vGurad_main/pull/5)
- [Update README.md](https://github.com/KODEGAS/vGurad_main/pull/4)
- [Create README.md](https://github.com/KODEGAS/vGurad_main/pull/3)
- [Delete .github/workflows/deno.yml](https://github.com/KODEGAS/vGurad_main/pull/2)
- [Add automated Vercel deployment workflow with GitHub Actions](https://github.com/KODEGAS/vGurad_main/pull/1)

</details>

<details>
<summary><strong><a href="https://github.com/KODEGAS/website">KODEGAS/website</a></strong></summary>

- [Fix GitHub Actions: Add complete CI/CD pipeline with Firebase deployment](https://github.com/KODEGAS/website/pull/3)
- [Optimize website for minimal load time and comprehensive SEO - 68% performance improvement](https://github.com/KODEGAS/website/pull/2)
- [Implement comprehensive SEO optimization for KODEGAS website](https://github.com/KODEGAS/website/pull/1)

</details>

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
<summary><strong><a href="https://github.com/Maleesha101/ArenaXX">Maleesha101/ArenaXX</a></strong></summary>

- [DataBase Connected and Login UI Created](https://github.com/Maleesha101/ArenaXX/pull/1)

</details>

<details>
<summary><strong><a href="https://github.com/Rusiru-Randika/Modified_Background_Remove_V2">Rusiru-Randika/Modified_Background_Remove_V2</a></strong></summary>

- [Use that Public Link](https://github.com/Rusiru-Randika/Modified_Background_Remove_V2/pull/1)

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
<summary><strong><a href="https://github.com/gihan001/RESTAUTANTMNG-V1">gihan001/RESTAUTANTMNG-V1</a></strong></summary>

- [kavindu](https://github.com/gihan001/RESTAUTANTMNG-V1/pull/1)

</details>

<details>
<summary><strong><a href="https://github.com/lingdojo/kana-dojo">lingdojo/kana-dojo</a></strong></summary>

- [content: add new japan fact](https://github.com/lingdojo/kana-dojo/pull/20437)
- [content: add video game quote](https://github.com/lingdojo/kana-dojo/pull/20436)

</details>

<details>
<summary><strong><a href="https://github.com/maneeshaYasinth/robo-battle-page">maneeshaYasinth/robo-battle-page</a></strong></summary>

- [Footer Created (Not added WA No. etc)](https://github.com/maneeshaYasinth/robo-battle-page/pull/2)

</details>

<details>
<summary><strong><a href="https://github.com/niro1-1/notebook-utils">niro1-1/notebook-utils</a></strong></summary>

- [feat: implement rate limiting and unit tests for failure scenarios (#32)](https://github.com/niro1-1/notebook-utils/pull/67)

</details>

<details>
<summary><strong><a href="https://github.com/sthmu/RESTAUTANTMNG-V1">sthmu/RESTAUTANTMNG-V1</a></strong></summary>

- [Kavindu](https://github.com/sthmu/RESTAUTANTMNG-V1/pull/2)

</details>

---

<sub>*Prior work as [kavindus0](https://github.com/kavindus0) is archived.*</sub>

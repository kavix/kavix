#!/usr/bin/env python3
"""
Automated profile README updater for kavix.
Fetches latest open-source PRs and memberships via GitHub API,
and formats the README.md accordingly.
"""

import os
import sys
import json
import urllib.request
import urllib.error

GITHUB_USER = "kavix"
ARCHIVED_USER = "kavindus0"

# Category definitions and repository mappings
REPO_CATEGORY_MAP = {
    # Cloud Native & Kubernetes
    "GoogleContainerTools/skaffold": "Cloud Native & Kubernetes",
    "kgateway-dev/kgateway": "Cloud Native & Kubernetes",
    "kubernetes-sigs/cloud-provider-azure": "Cloud Native & Kubernetes",
    "kubernetes-sigs/inference-perf": "Cloud Native & Kubernetes",
    "kubernetes-sigs/kueue": "Cloud Native & Kubernetes",
    "kubernetes/kubernetes": "Cloud Native & Kubernetes",
    "ray-project/kuberay": "Cloud Native & Kubernetes",

    # Developer Platforms & IDP
    "guidewire-oss/teams360": "Developer Platforms & IDP",
    "guidewire-oss/teamhealthcheck": "Developer Platforms & IDP",
    "openchoreo/backstage-plugins": "Developer Platforms & IDP",
    "openchoreo/openchoreo": "Developer Platforms & IDP",
    "openchoreo/openchoreo.github.io": "Developer Platforms & IDP",
    "openchoreo/sample-gitops": "Developer Platforms & IDP",
    "Yeachan-Heo/oh-my-claudecode": "Developer Platforms & IDP",

    # Identity, Access Management & Security
    "Hushield/hushield": "Identity, Access Management & Security",
    "asgardeo/javascript": "Identity, Access Management & Security",
    "smallstep/cli": "Identity, Access Management & Security",
    "thunder-id/thunderid": "Identity, Access Management & Security",
    "wso2/azure-terraform-modules": "Identity, Access Management & Security",
    "wso2/carbon-identity-framework": "Identity, Access Management & Security",
    "wso2/healthcare-accelerator": "Identity, Access Management & Security",
    "wso2/product-is": "Identity, Access Management & Security",

    # Compilers, Runtimes & Languages
    "apple/container": "Compilers, Runtimes & Languages",
    "ballerina-platform/ballerina-lang": "Compilers, Runtimes & Languages",
    "ballerina-platform/module-ballerina-http": "Compilers, Runtimes & Languages",
    "crate-ci/cargo-release": "Compilers, Runtimes & Languages",
    "facebook/pyrefly": "Compilers, Runtimes & Languages",
    "modular/modular": "Compilers, Runtimes & Languages",
    "wso2/mi-vscode": "Compilers, Runtimes & Languages",

    # AI, Vision & Research
    "facebookresearch/projectaria_tools": "AI, Vision & Research",

    # Other Open Source Contributions
    "LDFLK/OpenGIN": "Other Open Source Contributions",
    "LDFLK/openginxplore": "Other Open Source Contributions",
    "Termix-SSH/Termix": "Other Open Source Contributions",
    "clencyc/LiveEdit": "Other Open Source Contributions",
    "lingdojo/kana-dojo": "Other Open Source Contributions",
    "niro1-1/notebook-utils": "Other Open Source Contributions",
}

CATEGORY_ORDER = [
    "Cloud Native & Kubernetes",
    "Developer Platforms & IDP",
    "Identity, Access Management & Security",
    "Compilers, Runtimes & Languages",
    "AI, Vision & Research",
    "Other Open Source Contributions",
]

# Repositories / authors to exclude from OSS showcase
EXCLUDED_OWNERS = {GITHUB_USER.lower(), ARCHIVED_USER.lower(), "kodegas"}
EXCLUDED_REPOS = {
    "maleesha101/arenaxx",
    "blackbossx/elektrum-backend",
    "kavishkadinajara/fileflow",
}


import ssl

def github_request(url: str, token: str = None) -> dict:
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": f"kavix-profile-updater",
    }
    if token:
        headers["Authorization"] = f"token {token}"
    req = urllib.request.Request(url, headers=headers)
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, context=ctx) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, ssl.SSLError):
        # Fallback if local certs are missing
        unverified_ctx = ssl._create_unverified_context()
        with urllib.request.urlopen(req, context=unverified_ctx) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code} for {url}: {e.read().decode('utf-8')}", file=sys.stderr)
        raise


def fetch_all_prs(token: str = None) -> list:
    prs = []
    page = 1
    while True:
        url = f"https://api.github.com/search/issues?q=author:{GITHUB_USER}+type:pr&sort=created&order=desc&per_page=100&page={page}"
        data = github_request(url, token)
        items = data.get("items", [])
        if not items:
            break
        prs.extend(items)
        if len(items) < 100 or len(prs) >= data.get("total_count", 0):
            break
        page += 1
    return prs


def check_k8s_membership(token: str = None) -> bool:
    try:
        # Check kubernetes-sigs membership
        url = f"https://api.github.com/orgs/kubernetes-sigs/members/{GITHUB_USER}"
        github_request(url, token)
        return True
    except Exception:
        # Fallback: check if membership issue exists and was merged/closed in kubernetes/org
        try:
            search_url = f"https://api.github.com/search/issues?q=repo:kubernetes/org+type:issue+author:{GITHUB_USER}+is:closed"
            data = github_request(search_url, token)
            return data.get("total_count", 0) > 0
        except Exception:
            return True


def determine_category(repo_full_name: str) -> str:
    if repo_full_name in REPO_CATEGORY_MAP:
        return REPO_CATEGORY_MAP[repo_full_name]

    # Heuristics for new repositories
    repo_lower = repo_full_name.lower()
    if any(k in repo_lower for k in ["kubernetes", "k8s", "kueue", "gateway", "cilium", "envoy", "cloud-provider", "helm"]):
        return "Cloud Native & Kubernetes"
    if any(k in repo_lower for k in ["backstage", "choreo", "devops", "platform", "portal"]):
        return "Developer Platforms & IDP"
    if any(k in repo_lower for k in ["auth", "security", "identity", "crypto", "shield", "iam"]):
        return "Identity, Access Management & Security"
    if any(k in repo_lower for k in ["compiler", "runtime", "lang", "parser", "type", "lsp", "formatter"]):
        return "Compilers, Runtimes & Languages"
    if any(k in repo_lower for k in ["ai", "research", "vision", "aria", "model", "llm", "diffusion"]):
        return "AI, Vision & Research"

    return "Other Open Source Contributions"


def generate_markdown(prs: list, is_k8s_member: bool) -> str:
    # Organize PRs by category -> repository -> list of PRs
    categories = {cat: {} for cat in CATEGORY_ORDER}

    for pr in prs:
        repo_url = pr["repository_url"]
        repo_name = "/".join(repo_url.split("/")[-2:])
        owner = repo_name.split("/")[0].lower()

        if owner in EXCLUDED_OWNERS or repo_name.lower() in EXCLUDED_REPOS:
            continue

        cat = determine_category(repo_name)
        if cat not in categories:
            categories[cat] = {}
        if repo_name not in categories[cat]:
            categories[cat][repo_name] = []

        categories[cat][repo_name].append({
            "title": pr["title"].strip(),
            "url": pr["html_url"],
            "number": pr["number"],
        })

    lines = []
    lines.append("")
    if is_k8s_member:
        lines.append("**Kubernetes Organization Member** ([`kubernetes-sigs`](https://github.com/kubernetes-sigs))")
        lines.append("")
    lines.append(f"<sub>*Prior work as [{ARCHIVED_USER}](https://github.com/{ARCHIVED_USER}) is archived.*</sub>")
    lines.append("---")
    lines.append("<details>")
    lines.append("<summary><h3>Open Source Contributions</h3></summary>")
    lines.append("")
    lines.append("<br>")
    lines.append("")

    for cat in CATEGORY_ORDER:
        repos = categories.get(cat, {})
        if not repos:
            continue

        lines.append(f"#### {cat}")
        lines.append("")

        for repo_name in sorted(repos.keys(), key=lambda s: s.lower()):
            pr_list = repos[repo_name]
            lines.append("<details>")
            lines.append(f"<summary><strong><a href=\"https://github.com/{repo_name}\">{repo_name}</a></strong></summary>")
            lines.append("")
            for p in pr_list:
                title = p["title"]
                lines.append(f"- [{title}]({p['url']})")
            lines.append("")
            lines.append("</details>")
            lines.append("")

    lines.append("</details>")
    lines.append("")

    return "\n".join(lines)


def main():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    print("Fetching PRs from GitHub...")
    prs = fetch_all_prs(token)
    print(f"Fetched {len(prs)} PRs.")

    is_k8s_member = check_k8s_membership(token)
    print(f"Kubernetes Org Member status: {is_k8s_member}")

    readme_content = generate_markdown(prs, is_k8s_member)

    readme_path = os.path.join(os.path.dirname(__file__), "..", "..", "README.md")
    readme_path = os.path.abspath(readme_path)

    current_content = ""
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            current_content = f.read()

    if current_content.strip() == readme_content.strip():
        print("README.md is already up to date. No changes made.")
    else:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(readme_content)
        print("Successfully updated README.md.")


if __name__ == "__main__":
    main()

# 보안 정책

<p><strong>한국어</strong> · <a href="#security-policy">English</a></p>

## 지원 버전

보안 수정은 최신 마이너 판에만 올립니다. 옛 판으로 되돌려 고쳐 드리지 않으니 올려서 쓰세요.

| 버전  | 보안 수정 |
| ----- | --------- |
| 0.1.x | 지원      |

이 표의 지원 판은 `plugin/.claude-plugin/plugin.json` 의 버전을 따릅니다. 둘이 어긋나면 CI 의 `버전 표기 일치` 작업이 막습니다.

## 신고 방법

취약점을 공개 이슈로 올리지 말아 주세요. 다음 두 가지 중 하나를 씁니다.

1. [Security → Report a vulnerability](https://github.com/IsthisLee/korean-kit/security/advisories/new) 로 비공개 신고
2. 메일 `rjsgmldnwn@gmail.com`

받은 날부터 영업일 기준 5일 안에 접수 여부를 알려 드립니다. 수정이 필요하면 패치와 함께 권고문을 공개하고 신고자가 원하면 이름을 올립니다.

## 이 플러그인이 하는 일

설치해도 자동으로 도는 프로그램은 없습니다. 스킬을 부를 때만 스크립트가 돕니다. 2026-09-17 에 편집 뒤 자동으로 돌던 검사 훅을 뺐습니다.

| 항목        | 실제                                                                              |
| ----------- | --------------------------------------------------------------------------------- |
| 실행 시점   | 윤문이나 글자 수 스킬을 부를 때만                                                 |
| 실행하는 것 | `plugin/scripts/*.py`(python3)와 `plugin/skills/korean-character-count/scripts/*.js`(node) |
| 읽는 것     | 윤문할 원문과 스킬이 참조하는 규칙집 파일                                          |
| 쓰는 것     | 윤문할 때 작업 폴더의 `_workspace/` 에 입력과 결과 파일                            |
| 네트워크    | 쓰지 않습니다. 원문은 이 컴퓨터 밖으로 나가지 않습니다                            |
| 외부 의존성 | 없습니다. 표준 라이브러리만 씁니다                                                 |

네트워크를 쓰지 않는다는 것은 직접 확인할 수 있습니다. 아래 두 명령 모두 아무것도 내놓지 않아야 정상입니다.

```bash
# 1. 네트워크 호출 — 출력 없음
grep -nE 'curl|wget|urllib|requests|socket|urlopen|http\.client|import ssl' plugin/scripts/*.py plugin/skills/humanize-korean/references/*.py

# 2. 외부 프로그램 실행 — 출력 없음
grep -nE 'subprocess|os\.system|popen|exec\b' plugin/scripts/*.py plugin/skills/humanize-korean/references/*.py
```

## 끄는 방법

| 범위        | 방법                                     |
| ----------- | ---------------------------------------- |
| 한 번만     | 스킬을 부르지 않으면 아무것도 돌지 않습니다 |
| 완전히 제거 | `claude plugin uninstall korean-kit` |

## 범위 밖

스킬 파일은 모델이 읽는 지시문이고 실행 코드가 아닙니다. 윤문 파이프라인의 파이썬 스크립트(`plugin/scripts/*.py`, `plugin/skills/humanize-korean/references/*.py`, im-not-ai 에서 내장)는 윤문 요청이 있을 때만 돌고 작업 폴더의 `_workspace/` 에 입력과 결과 파일을 쓰며 네트워크를 쓰지 않습니다. 이 문서의 약속은 이 파일들에도 해당합니다. 취약점 신고 대상은 실제로 실행되는 `plugin/scripts/` 와 `plugin/skills/korean-character-count/scripts/` 입니다.

---

<a id="security-policy"></a>

# Security Policy

<p><a href="#보안-정책">한국어</a> · <strong>English</strong></p>

## Supported versions

Security fixes land on the latest minor only. Older lines are not backported, so upgrade.

| Version | Security fixes |
| ------- | -------------- |
| 0.1.x   | Supported      |

This table tracks the version in `plugin/.claude-plugin/plugin.json`. The `버전 표기 일치` CI job fails if the two drift apart.

## Reporting a vulnerability

Please do not open a public issue. Use one of these instead:

1. [Security → Report a vulnerability](https://github.com/IsthisLee/korean-kit/security/advisories/new) (private)
2. Email `rjsgmldnwn@gmail.com`

You will get an acknowledgement within 5 business days. If a fix is needed, an advisory is published alongside the patch, and reporters are credited on request.

## What this plugin does

Nothing runs automatically after installation. Scripts run only when you invoke a skill. The edit-time check hook was removed on 2026-09-17.

| Item             | Reality                                                                        |
| ---------------- | ------------------------------------------------------------------------------ |
| When it runs     | Only when you invoke the polishing or character-count skill                     |
| What it executes | `plugin/scripts/*.py` (python3) and `plugin/skills/korean-character-count/scripts/*.js` (node) |
| What it reads    | The text you ask it to polish and the reference files the skill cites           |
| What it writes   | Input and result files under `_workspace/` in the working directory             |
| Network          | None. Your text never leaves your machine                                       |
| Dependencies     | None. Standard library only                                                     |

You can verify the network claim yourself. Both commands should print nothing:

```bash
# 1. Network calls - no output
grep -nE 'curl|wget|urllib|requests|socket|urlopen|http\.client|import ssl' plugin/scripts/*.py plugin/skills/humanize-korean/references/*.py

# 2. Spawning external programs - no output
grep -nE 'subprocess|os\.system|popen|exec\b' plugin/scripts/*.py plugin/skills/humanize-korean/references/*.py
```

## Turning it off

| Scope       | How                                      |
| ----------- | ---------------------------------------- |
| Per use     | Do not invoke the skill; nothing runs     |
| Remove it   | `claude plugin uninstall korean-kit` |

## Out of scope

Skill files are instructions the model reads, not code that runs. The polishing pipeline's Python scripts (`plugin/scripts/*.py` and `plugin/skills/humanize-korean/references/*.py`, vendored from im-not-ai) run only on a polish request, write input and result files under `_workspace/` in the working directory, and use no network. The promises in this document cover those files as well. Vulnerability reports apply to `plugin/scripts/` and `plugin/skills/korean-character-count/scripts/`.

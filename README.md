<p align="center">

<a href="https://github.com/IsthisLee/korean-kit/actions/workflows/validate.yml"><img alt="Validate" src="https://github.com/IsthisLee/korean-kit/actions/workflows/validate.yml/badge.svg?branch=main"></a>
<a href="https://github.com/IsthisLee/korean-kit/actions/workflows/codeql.yml"><img alt="CodeQL" src="https://github.com/IsthisLee/korean-kit/actions/workflows/codeql.yml/badge.svg?branch=main"></a>
<img alt="MIT" src="https://img.shields.io/badge/license-MIT-blue.svg">
<img alt="Claude Code Plugin" src="https://img.shields.io/badge/Claude%20Code-plugin-8A2BE2">
<img alt="version" src="https://img.shields.io/badge/version-0.1.0-lightgrey">
<img alt="network" src="https://img.shields.io/badge/network-none-success">
<a href="https://github.com/IsthisLee/korean-ai-signals"><img alt="analysis" src="https://img.shields.io/badge/analysis-korean--ai--signals-informational"></a>

</p>

<picture>

  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/hero.svg">

  <source media="(prefers-color-scheme: light)" srcset="docs/assets/hero-light.svg">

  <img src="docs/assets/hero.svg" alt="korean-kit: 내가 쓰려고 분석한 한국어 도구들을 묶은 Claude Code 플러그인" width="100%">

</picture>

<p align="center">

<strong>내가 쓰려고 다양한 한국어 도구들을 분석하고, 원하는 것만 묶고 맘대로 커스텀한 Claude Code 플러그인</strong><br>  
무엇을 묶을지는 사람이 쓴 글과 Claude가 쓴 글을 직접 비교해 정합니다.

</p>

<p align="center">
<a href="#이-플러그인은">소개</a> ·
<a href="#묶은-것">묶은 것</a> ·
<a href="#설치">설치</a> ·
<a href="#사용법">사용법</a> ·
<a href="#어떻게-골랐나">고른 기준</a> ·
<a href="#분석-결과">분석 결과</a> ·
<a href="#분석-도구">분석 도구</a> ·
<a href="#원칙">원칙</a> ·
<a href="#기여">기여</a>
</p>

> [!NOTE]
> 표본은 학습에 사용하지 않습니다.
>
> 한국어 검사 도구를 검증하는 용도로만 사용합니다.

> [!IMPORTANT]
> 이 README는 [분석 계획](https://github.com/IsthisLee/korean-ai-signals/blob/main/docs/plan.md)을 모두 마친 상태를 기준으로 썼습니다. 사람 글 487편은 모았고 본 측정은 아직 돌리지 않아서 「측정 전」이라고 적힌 칸에는 결과가 없습니다.

## 이 플러그인은

한국어 윤문 도구를 output style 로 켜 두고 늘 적용했더니 문제가 생겼습니다. **답변에서 내용이 생략되고 뜻이 사라졌습니다.** 문장은 매끄러워졌는데 원래 있던 사실과 설명이 함께 깎여 나갔습니다.

그래서 뜻을 덜 잃는 도구를 찾기로 했습니다. 늘 켜 두는 한국어 도구 가운데 의미 손실을 막는 데 집중한 [fluent-korean](https://github.com/snflkd/fluent-korean) 을 찾아 지금 쓰고 있습니다. 이것을 플러그인에 실을지는 아래 비교 결과로 정합니다.

다만 그때 고른 방법은 도구 설명을 읽고 직접 써 보는 것이었습니다. 몇몇 도구는 KatFishNet(ACL 2025) 같은 연구를 근거로 달아 두었고, 아무 출처도 적지 않은 도구도 있었습니다. **어느 쪽이든 제 글에서 어느 도구가 뜻을 덜 잃는지는 알 수 없었습니다. 뜻 손실을 세는 기준이 없었기 때문입니다.**

그래서 도구를 고르는 근거를 사람이 쓴 글과 Claude가 쓴 글의 직접 비교에서 얻기로 했습니다. 두 글을 실제로 가르는 신호로 검사기를 만들고 그 검사기로 문체 도구와 윤문 도구를 같은 조건에서 견줍니다. **사람 글 487편은 모았고 그다음 단계는 아직 돌리지 않았습니다(진행 예정).** 지금 묶은 것은 비교를 마치기 전에 고른 것이고 결과가 나오면 그 기준으로 다시 정합니다. 묶은 도구는 제 작업 방식에 맞게 고쳤습니다. 모두에게 맞추려는 범용 도구가 아니라 제가 쓰려고 만든 묶음입니다.

도구를 고르는 기준은 두 가지이고 첫째가 둘째보다 앞섭니다.

1. **의미가 절대 손실되지 않는 명확한 한국어**
2. **번역체 교정과 AI 표현 최소화**

뜻을 하나라도 잃은 도구는 AI 티가 아무리 적어도 묶지 않습니다. 첫째를 둘째보다 앞에 둔 이유가 위에서 겪은 일입니다.

## 묶은 것

| 기능             | 하는 일                                                  | 어떻게 골랐나                                                                              | 가져온 곳                                                                           |
| ---------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| **윤문**         | 이미 쓴 글을 사실과 숫자는 그대로 두고 문체만 다듬습니다 | 후보 9개를 같은 원문에 돌려, 뜻 손실이 0건인 도구 가운데 AI 신호가 가장 적은 것을 묶습니다 | 측정 전. 지금은 [im-not-ai](https://github.com/epoko77-ai/im-not-ai) 커밋 `9747f03` |
| **글자 수**      | 한국어 글자 수를 모델이 어림잡지 않고 스크립트로 셉니다  | 세기만 하는 도구라서 비교하지 않았습니다                                                   | [k-skill](https://github.com/NomaDamas/k-skill)                                     |
| **output style** | 평소 답변과 처음 쓰는 글의 문체를 정합니다               | 후보를 같은 요청에 켜고 비교해, 뜻 손실이 0건인 것 가운데 가장 자연스러운 것을 싣습니다    | 측정 전(진행 예정)                                                                  |

**output style 은 이 플러그인이 직접 싣습니다.** 예전에는 따로 깔라고 안내했는데, 플러그인이 `output-styles/` 디렉터리로 실을 수 있어 그렇게 바꿉니다. 어느 것을 실을지는 비교 결과로 정합니다. 켜고 끄는 법과 주의할 점은 [사용법](#사용법)에 있습니다.

플러그인에 넣지 않는 것이 하나 있습니다. **AI 신호 검사기(진행 예정)** 는 글 한 편의 AI 신호 점수를 내고 문턱을 넘으면 알리기만 합니다. 사람 글 487편과 Claude 글 487편으로 만듭니다. 끝까지 손대지 않은 시험 자료의 사람 글 122편에서 한 편도 잡지 않는지 확인합니다. 만들면 [korean-ai-signals](https://github.com/IsthisLee/korean-ai-signals) 에 두고 설치본에는 넣지 않습니다. 형태소 분석기가 필요해서 설치본에 넣으면 의존성이 생깁니다.

### 묶으며 고친 것

| 도구            | 고친 것                                                                                                                                      |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| im-not-ai 윤문  | 런타임에 쓰는 스킬 셋, 에이전트 셋, 스크립트 아홉만 가져왔고, `humanize-korean` 설명의 트리거 문구 "AI detector bypass 한글" 하나만 뺐습니다 |
| k-skill 글자 수 | 스크립트는 그대로 두고 실행 경로를 고쳤으며, 스킬 설명은 원본을 바탕으로 다시 썼습니다                                                       |

비교 결과로 윤문 도구를 바꾸면 이 표와 [plugin/NOTICE.md](plugin/NOTICE.md)를 함께 고칩니다.

### 뺀 것

써 보고 뺀 기능입니다. 경위는 [CHANGELOG.md](CHANGELOG.md)에 있습니다.

| 뺀 것                                       | 이유                                                                                                                                                                                  |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 평소 답변과 서브에이전트에 문체 규칙 주입   | 규칙을 넣으면 답에서 기본값 같은 세부가 빠졌습니다. 같은 길이의 중립 문장을 넣었을 때는 빠지지 않아, 길이가 아니라 규칙 내용이 원인이었습니다. 맨 위에 적은 겪은 일과 같은 현상입니다 |
| 이 플러그인이 쓰던 작성 스킬과 output style | 평소 답변과 처음 쓰는 글의 문체는 사용자가 고른 output style 에 맡겼습니다. 지금은 그 후보를 이 플러그인이 싣는 쪽으로 정했고, 무엇을 실을지는 비교 결과로 정합니다                   |

## 설치

```bash
claude plugin marketplace add IsthisLee/korean-kit
claude plugin install korean-kit
```

`claude plugin list` 에 `korean-kit` 이 `enabled` 로 보이면 끝입니다. 새 버전은 `claude plugin update korean-kit` 으로 받습니다. 문체를 정하는 output style 도 이 플러그인이 싣습니다. 무엇을 실을지는 비교 결과로 정합니다. 켜는 것은 쓰는 사람이 [사용법](#output-style-켜고-끄기)에서 고릅니다.

| 필요한 것           | 어디에 쓰나             | 없으면                   |
| ------------------- | ----------------------- | ------------------------ |
| Claude Code         | 전부. 2.1.274 에서 확인 | 쓸 수 없습니다           |
| `python3` 3.10 이상 | 윤문 스크립트           | 윤문을 쓸 수 없습니다    |
| `node` 18+          | 글자 수 스크립트        | 그 스킬만 쓸 수 없습니다 |

CI가 macOS와 Linux에서 같은 검사를 돌립니다. Windows는 Git Bash나 WSL이 필요하고 아직 돌려 보지 않았습니다.

## 사용법

평소처럼 말하면 됩니다.

```
아래 글 번역투만 고쳐줘. 사실과 숫자는 그대로 두고.
이 자기소개서 공백 포함 몇 자야? 1,000자 제한이야.
이번 배포 QA 보고서를 배포-QA.md로 써줘.
```

| 무엇이   | 저절로 도는 때                            | 직접 부르는 명령                           |
| -------- | ----------------------------------------- | ------------------------------------------ |
| 윤문     | "AI 티 없애줘", "번역투 고쳐줘" 같은 요청 | `/korean-kit:humanize [글 또는 파일 경로]` |
| 2차 윤문 | 저절로 돌지 않습니다                      | `/korean-kit:humanize-redo [지시]`         |
| 글자 수  | "500자 이내로", "글자 수 세줘" 같은 요청  | `/korean-kit:korean-character-count`       |

### output style 켜고 끄기

문체는 output style 이 맡습니다. 이 플러그인이 싣는 것은 고르는 목록에 나타나고 **설치했다고 저절로 켜지지 않습니다.** 켜는 것은 쓰는 사람이 정합니다.

```
/config  →  Output style  →  korean-kit:<이름>
```

고른 값은 `.claude/settings.local.json` 의 `outputStyle` 에 저장됩니다. 손으로 적어도 됩니다.

```json
{ "outputStyle": "korean-kit:<이름>" }
```

끄려면 같은 자리에서 `default` 를 고릅니다. 예전에 쓰던 `/output-style` 명령은 v2.1.73 에서 폐기되고 v2.1.91 에서 없어졌습니다.

> [!WARNING]
> **켜면 값을 치릅니다. 세 가지를 알고 켜세요.**
>
> 1. **문체 지침이 매 요청에 함께 갑니다.** 참고로 지금 나와 있는 한국어 output style 하나는 2,681자(어림 2,600~3,200토큰)입니다. 프롬프트 캐시가 첫 요청 뒤의 비용을 줄이지만 0이 되지는 않습니다.
> 2. **출력이 길어집니다.** 조사와 어미, 문장 성분을 생략하지 말라는 지침이라 같은 내용을 쓰는 데 글자가 더 듭니다.
> 3. **코딩 지침을 대체할 수 있습니다.** output style 은 Claude Code 의 기본 지침을 바꾸는 장치여서 스타일 파일에 `keep-coding-instructions: true` 가 없으면 코드 작업 지침이 통째로 빠집니다. 이 플러그인이 싣는 것은 그 값을 켠 판으로 만듭니다.
>
> 출처: [Output styles](https://code.claude.com/docs/en/output-styles) (2026-09-18 확인)

## 어떻게 골랐나

### 무엇이 근거가 되지 못했나

도구를 고르려면 기댈 것이 필요했는데, 손에 잡히는 것들이 차례로 무너졌습니다.

1. **널리 퍼진 AI 티 목록.** 한국어 AI 글을 사람 글과 직접 비교한 연구를 찾아보니 두 편뿐이었고 그중 지표를 공개한 KatFishNet(ACL 2025)이 검증한 것이 8개였습니다. 흔히 말하는 줄표·복수형 `-들`·「A가 아니라 B」 대구는 그런 연구를 찾지 못했습니다.
2. **AI 탐지기의 판정.** 영어 AI 탐지기가 비원어민이 쓴 글을 AI 글로 잘못 분류했다는 연구가 있습니다([Liang 외 2023](https://arxiv.org/abs/2304.02819)). 사람 글을 AI 글로 잘못 잡는 것은 놓치는 것보다 해롭습니다.
3. **이 저장소가 예전에 쓰던 규칙과 그 측정.** 규칙의 안내대로 고친 대조 글에서 정보가 사라지거나 문장을 잇는 말이 빠졌습니다. 사람이 쓴 글인지를 파일 수정 연도로 짐작했고 합격선을 결과를 본 뒤에 적기도 했습니다.

남은 방법은 직접 재는 것뿐이었습니다.

### 비교 순서

기준을 결과보다 먼저 [분석 계획](https://github.com/IsthisLee/korean-ai-signals/blob/main/docs/plan.md)에 적고 커밋하는 것으로 시작합니다. 파일럿을 두 번 돌려 방법을 고친 뒤, ChatGPT가 공개된 2022-11-30 이전의 사람 글 487편을 모으고 같은 제목과 장르로 Claude 글을 487편 씁니다. 짝마다 길이를 맞춰 자른 다음 KatFishNet이 한국어에서 검증한 지표 8개를 재고 훈련 자료로 문서 점수를 만듭니다. 문턱은 훈련·개발 자료로 정하고 끝까지 손대지 않은 시험 자료 122편에 한 번만 적용해 오탐을 잽니다. 마지막으로 통하는 지표를 검사 규칙으로 옮기고 도구를 견줘 무엇을 묶을지 정합니다.

표본 수, 자료를 나누는 비율, 단계마다의 판정 기준은 계획서에 있습니다. 정본은 그쪽이고 이 README에는 결과만 옮깁니다.

### 도구 비교 기준

1. **뜻 손실이 0건인 도구만 남깁니다.** 원문이나 요청에 담긴 사실을 목록으로 미리 만들고 결과 글에서 사라지거나 바뀌거나 새로 생긴 사실과 빠진 문장 성분을 셉니다. 1건이라도 있으면 탈락입니다.
2. **남은 도구는 자연스러움으로 줄 세웁니다.** 두 도구의 결과를 나란히 놓고 어느 쪽이 사람이 쓴 글에 가까운지 블라인드로 고르게 합니다. 쌍마다 순서를 바꿔 두 번 묻고 승패를 이항 검정으로 셉니다.
3. **자연스러움이 갈리지 않으면 AI 신호 밀도로 가립니다.** 검사기 점수를 1,000자당으로 세고 사람 글의 값을 기준선으로 함께 적습니다.
4. **그래도 같으면 명확성으로 가립니다.** 주어나 지시 대상이 모호한 곳을 셉니다.

자연스러움을 AI 신호 밀도보다 앞에 둔 이유가 있습니다. 표지를 적게 만드는 것과 잘 읽히게 만드는 것은 다릅니다. 이 저장소에서 규칙을 늘려 표지를 크게 줄인 판이 블라인드 쌍대 판정에서 옛 판을 이기지 못한 적이 있습니다(5승 6패).

뜻 손실은 claude-opus-5 가 순서를 바꿔 두 번 판정하고 판정의 일부는 사람이 원문과 대조합니다. 원문을 얼마나 바꿨는지(변경률)도 기록해서 과하게 고친 경우를 가려냅니다. 판정 기준 전문은 [분석 계획 8절](https://github.com/IsthisLee/korean-ai-signals/blob/main/docs/plan.md#8-도구-비교)에 있습니다.

## 분석 결과

본 측정을 마치면 채웁니다. 방법과 판정 기준은 [분석 계획](https://github.com/IsthisLee/korean-ai-signals/blob/main/docs/plan.md)에 결과보다 먼저 적어 두었습니다.

<details>
<summary><strong>결과표 셋 — 지금은 모두 「측정 전」입니다</strong></summary>

### AI 신호 검사기

| 항목                                          | 결과              |
| --------------------------------------------- | ----------------- |
| 시험 자료 사람 글 122편 가운데 문턱을 넘은 글 | 측정 전(기준 0편) |
| 문턱을 넘은 Claude 글                         | 측정 전           |
| AUROC 전체                                    | 측정 전           |
| AUROC 위키백과 / 기술 블로그 / 개인 블로그    | 측정 전           |
| AUROC claude-opus-5 / claude-sonnet-5         | 측정 전           |
| 채택한 지표와 문턱                            | 측정 전           |

AUROC는 사람 글과 Claude 글을 한 편씩 짝지었을 때 Claude 글의 점수가 더 높은 비율입니다. 0.5이면 두 글을 가르지 못하는 것이고 1이면 완전히 가르는 것입니다.

### output style

| output style                                             | 라이선스 | 뜻 손실 | 자연스러움 | AI 신호 밀도(1,000자당) | 명확성  | 판정      |
| -------------------------------------------------------- | -------- | ------- | ---------- | ----------------------- | ------- | --------- |
| 기준선(아무것도 켜지 않음)                               | —        | 측정 전 | 측정 전    | 측정 전                 | 측정 전 | 비교 기준 |
| [fluent-korean](https://github.com/snflkd/fluent-korean) | MIT      | 측정 전 | 측정 전    | 측정 전                 | 측정 전 | 측정 전   |

output style 로 배포되는 한국어 플러그인은 2026-09-15 까지 이것 하나를 찾았습니다.

### 윤문 도구

| 도구                                                                                  | 라이선스   | 뜻 손실    | 자연스러움 | AI 신호 밀도(1,000자당) | 명확성     | 변경률     | 판정             |
| ------------------------------------------------------------------------------------- | ---------- | ---------- | ---------- | ----------------------- | ---------- | ---------- | ---------------- |
| [k-skill](https://github.com/NomaDamas/k-skill) `korean-humanizer`                    | MIT        | 측정 전    | 측정 전    | 측정 전                 | 측정 전    | 측정 전    | 측정 전          |
| [im-not-ai](https://github.com/epoko77-ai/im-not-ai) `humanize-korean` (지금 묶은 것) | MIT        | 측정 전    | 측정 전    | 측정 전                 | 측정 전    | 측정 전    | 측정 전          |
| [claude-forge](https://github.com/sangrokjung/claude-forge) `humanize-korean`         | MIT        | 측정 전    | 측정 전    | 측정 전                 | 측정 전    | 측정 전    | 측정 전          |
| [patina](https://github.com/devswha/patina)                                           | MIT        | 측정 전    | 측정 전    | 측정 전                 | 측정 전    | 측정 전    | 측정 전          |
| [DaleSeo/korean-skills](https://github.com/DaleSeo/korean-skills) `humanizer`         | MIT        | 측정 전    | 측정 전    | 측정 전                 | 측정 전    | 측정 전    | 측정 전          |
| [korean-report-skills](https://github.com/JangHyun-bin/korean-report-skills)          | Apache-2.0 | 측정 전    | 측정 전    | 측정 전                 | 측정 전    | 측정 전    | 측정 전          |
| [korean-prose-skill](https://github.com/JellyBrick/korean-prose-skill)                | **없음**   | 측정 안 함 | 측정 안 함 | 측정 안 함              | 측정 안 함 | 측정 안 함 | **묶을 수 없음** |
| [yoonmoon](https://github.com/amondnet/yoonmoon)                                      | MIT        | 측정 전    | 측정 전    | 측정 전                 | 측정 전    | 측정 전    | 측정 전          |
| [stop-slop-ko](https://github.com/limleesol/stop-slop-ko)                             | MIT        | 측정 전    | 측정 전    | 측정 전                 | 측정 전    | 측정 전    | 측정 전          |

k-skill 의 맞춤법 검사기는 외부 서비스의 이용 조건 때문에 대량 측정에서 뺍니다.

라이선스는 2026-09-18 에 GitHub API 로 확인했습니다. `korean-prose-skill` 은 LICENSE 파일도 README 의 언급도 없어 기본값인 「모든 권리 유보」입니다. 재배포가 막히므로 측정 결과와 무관하게 묶을 수 없습니다. 그래서 재지 않고 후보 목록에만 남깁니다. `korean-report-skills` 는 Apache-2.0 이라 묶게 되면 NOTICE 고지 조건이 더 붙습니다.

</details>

## 분석 도구

무엇을 묶을지 정하는 데 쓴 분석 도구는 별도 저장소 [korean-ai-signals](https://github.com/IsthisLee/korean-ai-signals) 에 있습니다. 사람 글과 Claude 글을 모으는 수집기, 지표를 재는 측정기, 결과보다 먼저 적은 [분석 계획](https://github.com/IsthisLee/korean-ai-signals/blob/main/docs/plan.md), 측정 결과가 모두 거기 있습니다. 형태소 분석기 Kiwi와 SciPy가 필요해서 이 플러그인과 따로 두었습니다. 준비 명령과 돌리는 순서는 그 저장소의 README에 있습니다. Claude 글을 새로 만들려면 로그인한 `claude` 명령이 필요하고 호출마다 비용이 듭니다. 모은 사람 글 본문과 Claude 글은 커밋하지 않고 출처 주소와 게시일을 적은 목록만 커밋합니다.

## 원칙

- **뜻이 먼저입니다.** 뜻을 잃은 도구는 AI 티가 적어도 묶지 않습니다.
- **사람 글을 잡는 것이 놓치는 것보다 나쁩니다.** 검사기의 문턱과 검사 규칙 모두 사람 글 0건을 먼저 봅니다.
- **기준은 결과보다 먼저 공개합니다.** 결과를 본 뒤 기준을 바꾸게 되면 원래 결과를 지우지 않고 사후 변경이라고 표시합니다.
- **3자 서비스와 통신하지 않습니다.** 설치본의 스킬과 스크립트는 네트워크를 쓰지 않습니다. 확인하는 명령은 [SECURITY.md](SECURITY.md)에 있습니다. 표본 수집과 Claude 글 생성은 저장소의 분석 스크립트만 하며 설치본에는 들어가지 않습니다.
- **가져온 파일은 가져온 대로 둡니다.** 출처와 고친 줄은 [plugin/NOTICE.md](plugin/NOTICE.md)에 있습니다.
- **설치가 곧 적용은 아닙니다.** output style 은 목록에 올라갈 뿐이고 켜는 것은 쓰는 사람이 정합니다. 강제로 켜는 `force-for-plugin` 은 쓰지 않습니다.

**저장할 때 검사하는 훅은 지금 없습니다.** 근거 없이 정한 규칙을 걷어냈고 비교 분석에서 통하는 지표가 나오면 그것으로 다시 만듭니다(진행 예정).

## 저장소 구성

`plugin/` 만 설치한 사람의 기계로 복사됩니다. CI와 관리자 스크립트, 저장소 문서는 그 밖에 둡니다.

```
korean-kit/
├── plugin/          설치본: 매니페스트, 윤문 스킬·에이전트, 글자 수 스킬
├── .claude-plugin/  마켓플레이스 매니페스트
├── tools/           가드, 릴리스, 그림 스크립트
├── docs/assets/     README 와 소셜 카드 그림
├── docs/samples/    실제 실행 기록 예시
├── .github/         CI 와 이슈 양식
└── .githooks/       커밋 직전 가드
```

## 기여

제 작업에 맞춘 묶음이지만 제보는 반깁니다. 절차는 [CONTRIBUTING.md](CONTRIBUTING.md)에 있습니다. 윤문이 뜻을 바꾸거나 스크립트가 죽었다면 [버그 제보](https://github.com/IsthisLee/korean-kit/issues/new?template=bug.yml)로 고치지 않은 원문 그대로 보내 주세요. 받아서 확인하는 명령은 이렇습니다.

```bash
python3 -m py_compile plugin/scripts/*.py
node plugin/skills/korean-character-count/scripts/korean_character_count.js --text "가나다" --format text
```

## 출처와 라이선스

윤문 스킬·에이전트·스크립트는 [im-not-ai](https://github.com/epoko77-ai/im-not-ai) 커밋 `9747f03`, 글자 수 스킬은 [k-skill](https://github.com/NomaDamas/k-skill)에서 가져왔습니다. 가져온 파일의 라이선스는 모두 MIT이고 원 저작권 표시는 [plugin/NOTICE.md](plugin/NOTICE.md)에 있습니다. 이 저장소의 라이선스도 [MIT](LICENSE)입니다.

---

<p align="center"><sub>Built with <a href="https://claude.com/claude-code">Claude Code</a> · <a href="./LICENSE">MIT</a></sub></p>

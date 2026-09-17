# CLAUDE.md

이 저장소에서 작업하는 Claude Code 를 위한 규칙입니다. 사람이 읽어도 됩니다.

## 이 저장소가 무엇인가

한국어 글을 다듬는 도구를 묶은 Claude Code 플러그인입니다. im-not-ai 에서 내장한 윤문 스킬 셋과 에이전트 셋, k-skill 에서 가져온 글자 수 스킬로 이루어집니다. 구조와 사용법은 [README.md](README.md) 에 있습니다.

무엇이 AI 티인지 사람 글과 Claude 글을 비교해 정하는 분석은 별도 저장소 [korean-ai-signals](https://github.com/IsthisLee/korean-ai-signals) 에 있습니다. 그 결과로 검사 규칙을 다시 만들면 이 저장소로 돌아옵니다.

**저장할 때 검사하는 훅은 지금 없습니다.** 2026-09-17 에 뺐습니다. 근거 없이 경험으로 정한 규칙이었고, 비교 분석에서 검증된 지표가 나오면 그것으로 다시 만들기로 했습니다. 훅을 되살리려면 분석이 채택한 지표에서 출발해야 하고, 사람 글을 잡지 않는다는 것을 표본으로 보여야 합니다.

## 저장소는 두 층이다

`plugin/` 만 설치한 사람의 기계로 갑니다. 나머지는 여기 남습니다.

```
plugin/     설치본. 매니페스트·스킬·에이전트·런타임 스크립트·LICENSE·NOTICE
tools/      관리자 스크립트(release·guard·그림 그리기)
docs/assets 그림
.github/    CI·이슈 양식·CI 전용 npm 도구
루트 문서    README·CHANGELOG·CONTRIBUTING·SECURITY·SUPPORT·CODE_OF_CONDUCT
```

**플러그인 설치는 `source` 가 가리키는 폴더를 통째로 복사하고 무엇을 빼는 수단이 없습니다.**
`.claude-plugin/marketplace.json` 의 `source` 가 `./plugin` 인 이유가 이것입니다. 실험·CI·저장소 문서를 `plugin/` 안에 두면 설치한 사람이 그것까지 내려받습니다.

새 파일을 어디에 둘지는 한 가지만 물으면 됩니다. **설치한 사람이 이것을 쓰는가.** 아니면 `plugin/` 밖입니다. CI 의 `설치본 경계` 작업이 CI 설정·관리자 스크립트·저장소 문서·잠금 파일이 `plugin/` 에 들어오는 것을 막고, `LICENSE`·`NOTICE.md`·매니페스트가 빠지는 것도 막습니다.

**설치는 작업 트리를 그대로 복사합니다. git 이 무시하는 파일도 따라갑니다.** 로컬에서 설치해 보기 전에 `find plugin -name __pycache__ -type d -exec rm -rf {} +` 로 치웁니다. CI 의 같은 작업이 `??` 와 `!!` 상태 파일을 막습니다.

경로를 옮길 때 같이 봐야 하는 곳은 `.gitattributes`(linguist), `.github/CODEOWNERS`, `.github/workflows/*.yml`, `.claude/settings.json` 의 권한 목록, `tools/*.sh` 입니다.

설치본이 제대로 도는지는 격리된 HOME 에 실제로 깔아 봅니다.

```bash
HOME=/tmp/kw-home claude plugin marketplace add "$PWD"
HOME=/tmp/kw-home claude plugin install korean-kit@korean-kit
find /tmp/kw-home/.claude/plugins/cache -type f | wc -l    # 설치본 파일 수
```

## 먼저 돌린다

```bash
python3 -m py_compile plugin/scripts/*.py                    # 내장 윤문 스크립트가 깨지지 않았는가
node plugin/skills/korean-character-count/scripts/korean_character_count.js --text "가나다" --format text
```

처음 받았으면 `git config core.hooksPath .githooks` 로 커밋 직전 검사를 켭니다. `tools/guard.sh` 가 홈 경로(`/Users/<이름>`)·세션 임시 경로·`.private/` 파일이 커밋에 섞이는 것을 막습니다. 개인 패턴을 더 막으려면 `.private/guard-patterns` 에 한 줄씩 적습니다. CI 의 「설치본 경계」 작업이 같은 가드를 저장소 전체에 돌립니다.

## 지켜야 하는 것

**네트워크를 쓰지 않습니다.** 스킬도 스크립트도 원문을 에이전트 외부로 보내지 않습니다. README 가 이것을 약속하고 있으므로, 네트워크 호출을 넣는 변경은 그 약속을 깨뜨립니다. 필요하다고 판단되면 코드를 넣기 전에 이슈로 먼저 논의합니다.

**규칙을 되살릴 때는 근거를 먼저 만듭니다.** 경험으로 정한 규칙을 다시 넣지 않습니다. 사람이 쓴 글과 Claude 가 쓴 글을 비교해 그 표현이 실제로 두 글을 가르는지 보이고, 사람 글을 잡지 않는다는 것을 표본으로 확인한 뒤에 넣습니다. 방법은 [korean-ai-signals 의 계획서](https://github.com/IsthisLee/korean-ai-signals/blob/main/docs/plan.md) 에 있습니다.

**한국어 글은 켜 둔 output style 을 따릅니다.** 커밋 메시지, README, 이슈 답변, 작업 메모가 모두 해당합니다.

## 건드리지 않는 것

`plugin/skills/humanize-korean/**`, `plugin/skills/humanize/**`, `plugin/skills/humanize-redo/**`, `plugin/agents/**`, `plugin/scripts/*.py`, `plugin/skills/korean-character-count/scripts/**` 는 다른 MIT 프로젝트에서 가져온 파일입니다. 출처와 수정 범위가 [plugin/NOTICE.md](plugin/NOTICE.md) 에 적혀 있습니다. 고쳐야 하면 그 파일의 해당 줄도 함께 고칩니다.

윤문 파이프라인은 im-not-ai 의 런타임 부분집합을 그대로 내장한 것입니다. 새 판을 받으려면 원본 저장소를 그 커밋으로 받아 같은 경로에 복사하고 plugin/NOTICE.md 에 적힌 한 줄 수정(트리거 문구)을 다시 적용한 뒤, `python3 -m py_compile plugin/scripts/*.py` 와 격리된 HOME 에서 `/korean-kit:humanize` 실행으로 확인하고 plugin/NOTICE.md 의 커밋을 올립니다. 스크립트는 `plugin/scripts/` 와 `plugin/skills/humanize-korean/references/` 의 상대 위치로 서로를 찾으므로 둘의 관계를 바꾸지 않습니다.

## 버전

정본은 `plugin/.claude-plugin/plugin.json` 한 곳입니다. README 배지와 마켓플레이스 매니페스트는 `tools/release.sh` 가 맞춰 줍니다. 손으로 따로 고치지 않습니다. CI 의 `버전 표기 일치` 작업이 어긋남을 잡습니다.

## 커밋

Conventional Commits 를 쓰고 제목은 한국어로 씁니다.

```
feat: 글자 수 스킬에 공백 제외 옵션을 더함
fix: 릴리스 태그 메시지에서 ### 헤딩이 주석으로 잘리던 문제
docs: 분석 저장소 분리를 기록함
```

# 기여 안내

기여를 환영합니다. 이 문서는 무엇을 보내면 좋은지, 보낸 것이 어떤 기준으로 받아들여지는지 적습니다.

## 가장 필요한 것은 실제 문장입니다

이 저장소는 무엇이 AI 티인지를 **Claude 가 실제로 쓴 문장**과 **사람이 쓴 문장**을 비교해 정합니다. 지어낸 나쁜 예는 만들기 쉽지만, 그것으로 기준을 정하면 현실에서 안 나오는 표현을 잡고 정작 나오는 표현을 놓칩니다.

그래서 가장 값진 기여는 코드가 아니라 문장입니다.

- Claude 가 쓴 어색한 한국어를 봤다면 [버그 이슈](https://github.com/IsthisLee/korean-writing/issues/new?template=bug.yml) 로 보내 주세요. 고치지 않은 원문 그대로가 필요합니다.
- 윤문이 뜻을 바꾸거나 사실을 지운 사례도 같은 양식으로 보내 주세요. 뜻을 잃는 것은 AI 티가 남는 것보다 심각합니다.

## 시작하기

빌드가 없습니다. 받아서 바로 돌리면 됩니다.

```bash
git clone https://github.com/IsthisLee/korean-writing
cd korean-writing
git config core.hooksPath .githooks   # 커밋 직전 검사: 개인 식별 정보 가드

python3 -m py_compile plugin/scripts/*.py
node plugin/skills/korean-character-count/scripts/korean_character_count.js --text "가나다" --format text
```

| 필요한 것 | 쓰는 곳          | 없으면              |
| --------- | ---------------- | ------------------- |
| `python3` | 윤문 스크립트    | 윤문을 못 씁니다    |
| `node`    | 글자 수 스크립트 | 그 스킬만 못 씁니다 |

macOS 와 Linux 에서 CI 가 돌고 있습니다. Windows 는 Git Bash 나 WSL 이 필요합니다.

## 검사 규칙을 넣으려면 근거가 있어야 합니다

저장할 때 검사하던 훅은 2026-09-17 에 뺐습니다. 경험으로 정한 규칙이었고 사람 글과 비교한 근거가 없었기 때문입니다.

규칙을 다시 넣는 변경은 **숫자를 함께 보내 주세요.** 필요한 것은 둘입니다.

1. 그 표현이 사람 글과 Claude 글을 실제로 가른다는 근거. 심사를 거친 연구이거나, 같은 제목으로 짝지은 표본에서 직접 잰 결과여야 합니다.
2. 사람이 쓴 글을 잡지 않는다는 확인. 표본에서 몇 편을 잡았는지 적습니다.

방법과 판정 기준은 분석 저장소의 [계획서](https://github.com/IsthisLee/korean-ai-signals/blob/main/docs/plan.md) 에 있습니다. 규칙 제안은 그 저장소의 이슈로 보내 주셔도 됩니다.

## 문서를 고치려면

한국어 문서는 읽는 사람이 한 번에 이해할 수 있게 씁니다. 문장 성분을 빼서 줄이지 않습니다.

## PR 보내기

1. 브랜치를 따서 작업합니다. `main` 에 직접 커밋하지 않습니다.
2. 위 검사를 로컬에서 통과시킵니다.
3. PR 을 엽니다. CI 가 macOS 와 Linux 양쪽에서 같은 검사를 돌립니다.

커밋 메시지는 Conventional Commits 를 쓰고 제목은 한국어로 씁니다.

```
feat: 글자 수 스킬에 공백 제외 옵션을 더함
fix: 릴리스 태그 메시지에서 ### 헤딩이 주석으로 잘리던 문제
docs: 분석 저장소 분리를 기록함
```

버전 번호는 손대지 마세요. `plugin/.claude-plugin/plugin.json` 이 정본이고 릴리스할 때 `tools/release.sh` 가 README 배지와 CHANGELOG 를 맞춥니다.

## 가져온 파일

`plugin/skills/humanize-korean/**`, `plugin/skills/humanize/**`, `plugin/skills/humanize-redo/**`, `plugin/agents/**`, `plugin/scripts/*.py`(im-not-ai), `plugin/skills/korean-character-count/scripts/**` 는 다른 MIT 프로젝트에서 가져왔습니다. 고쳐야 한다면 [plugin/NOTICE.md](plugin/NOTICE.md) 의 수정 범위도 함께 고쳐 주세요. 원 저작자의 저작권 표시는 지우지 않습니다.

## 규칙과 라이선스

참여하는 모든 사람은 [행동 강령](CODE_OF_CONDUCT.md) 을 따릅니다. 보안 문제는 공개 이슈 대신 [SECURITY.md](SECURITY.md) 의 절차를 씁니다.

보내 주신 기여는 이 저장소와 같은 [MIT 라이선스](LICENSE) 로 배포됩니다.

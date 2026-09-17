# Changelog

이 프로젝트의 눈에 띄는 변경을 기록합니다. 형식은 [Keep a Changelog](https://keepachangelog.com/ko/1.1.0/)를, 버전은 [SemVer](https://semver.org/lang/ko/)를 따릅니다.

## [Unreleased]

## [0.1.0] - 2026-09-18

첫 공개입니다.

이 묶음은 `korean-writing` 이라는 이름으로 먼저 만들었고 판 번호가 2.1.0 까지 갔습니다. **그때의 변경 기록과 릴리스는 남기지 않았습니다.** 그 판들의 중심은 저장할 때 검사하는 훅과 그 규칙이었는데, 사람 글과 비교한 근거가 없어 2026-09-17 에 통째로 뺐습니다. 남은 것이 그만큼 달라져서 옛 기록을 이어 붙이면 지금 무엇이 있는지 알기 어렵습니다. 판 번호를 0.1.0 으로 되돌리고 처음부터 셉니다.

### 묶은 것

- **윤문 스킬 셋과 에이전트 셋.** 이미 쓴 글을 사실과 숫자는 그대로 두고 문체만 다듬습니다. [im-not-ai](https://github.com/epoko77-ai/im-not-ai) 커밋 `9747f03` 에서 가져왔습니다. `/korean-kit:humanize` 와 `/korean-kit:humanize-redo` 로 부릅니다.
- **한국어 글자 수 스킬.** 글자 수를 어림하지 않고 스크립트로 셉니다. [k-skill](https://github.com/NomaDamas/k-skill) 에서 가져왔습니다. `/korean-kit:korean-character-count` 로 부릅니다.

가져온 파일의 출처와 수정 범위는 [plugin/NOTICE.md](plugin/NOTICE.md) 에 적혀 있습니다. 모두 MIT 입니다.

### 아직 없는 것

- **검사 규칙.** 무엇이 AI 티인지는 사람이 쓴 글과 Claude 가 쓴 글을 비교해 정하기로 했습니다. 그 분석은 [korean-ai-signals](https://github.com/IsthisLee/korean-ai-signals) 에서 하고 있고, 검증된 지표가 나오면 규칙으로 옮겨 여기에 넣습니다. 그때까지는 근거 없는 규칙을 두지 않습니다.

### 지켜야 하는 것

- **설치해도 저절로 도는 프로그램이 없습니다.** 스킬을 부를 때만 스크립트가 돕니다.
- **네트워크를 쓰지 않습니다.** 원문을 에이전트 밖으로 보내지 않습니다.

[Unreleased]: https://github.com/IsthisLee/korean-kit/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/IsthisLee/korean-kit/releases/tag/v0.1.0

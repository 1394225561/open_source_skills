# Official Source Provenance

This is a local provenance index, not an official MiniMax file.

## Source baseline

- Repository: `MiniMax-AI/MiniMax-H3`
- Local source: `D:\1_code-space\workspace_github\MiniMax-H3`
- Commit: `6da473b48daf91e5aebfb56451f8a0b116348df5`
- Commit date: 2026-08-13
- License date: 2026-08-02

## Unmodified official copies

`references/official-skills/` is an exact relative-path copy of the repository's complete `skills/` directory at the source baseline. It contains 36 files across:

- `h3-prompt-writing`
- `3d-animation-short-generator`
- `brand-promo-video-generator`
- `co-op-game-intro-generator`
- `handdrawn-live-video-generator`
- `minimalist-product-ad-generator`
- `music-video-subtitle-generator`
- `paper-collage-explainer-generator`
- `papercraft-stop-motion-explainer`
- The official `skills/README.md`

`references/official-repository/` contains unmodified copies of the repository's two root README files and all 18 scripts from `scripts/readme/`, preserving their original relative layout.

The skill-root `LICENSE` is an exact copy of the MiniMax H3 Community License Agreement supplied by the user. The skill-root `NOTICE` contains the notice required by Section III.4 of that agreement.

## Locally modified or original files

- `SKILL.md`: local H3 orchestration and progressive-loading entry point.
- `agents/openai.yaml`: local UI metadata.
- `h3-model-capabilities.md`: modified operational adaptation of official README and script facts; carries a prominent modification notice.
- `h3-production-patterns.md`: modified adaptation of selected official style-skill patterns plus local policy; carries a prominent modification notice.
- `h3-routing-and-handoffs.md`: local optional-specialist orchestration policy.
- `seedance-to-h3-adaptation.md`: local translation policy.
- This provenance index: local documentation of source boundaries.

## Scope boundary

This skill is not a complete mirror of the model repository. Model code, weights, architecture assets, demo videos/GIFs, environment files, and unrelated scripts are intentionally excluded because they are not prompt-writing or production-orchestration references.

Some links inside the unmodified official READMEs point to repository files outside the copied reference subset. Use the recorded local source repository when those non-bundled materials are genuinely needed.

## Update procedure

When updating from a later official commit:

1. Record the new commit hash and date.
2. Replace the unmodified official directories from the matching source paths without editing their contents.
3. Compare source and destination file sets bidirectionally by relative path.
4. Verify SHA-256 equality for every unmodified copied file.
5. Re-evaluate local adaptations against changed official facts and keep prominent modification notices.
6. Retain the applicable license and required notice; do not assume later licensing terms are unchanged.

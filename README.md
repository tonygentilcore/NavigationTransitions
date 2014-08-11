## What's Going On Here?

Navigation Transitions is a new browser feature that allows pages to coordinate on a transition animation which plays during navigation (even across origins). In addition to providing visual polish this may also improve the perception of speed and avoid interrupting users' flow of thought.

To understand the design and how you might build apps with Navigation Transitions, see the [explainer document](explainer.md).

## Spec and API Development

For the nitty-gritty of the API, the [draft W3C specification](//tonygentilcore.github.io/NavigationTransitions/spec/navigation_transitions/index.html) and [`navigation_transitions.ts`](//github.com/tonygentilcore/NavigationTransitions/blob/master/navigation_transitions.ts) are authoritative.

Spec development happens via [issues in this repository](issues).

Updates to the spec must reference [resolved issued marked `needs spec`](issues?labels=needs+spec&state=closed).

To edit the spec locally, you'll need a copy of [the Web Components-based framework which it is built with](//github.com/tonygentilcore/web-spec-framework). To fetch it, clone the repo and run:

```sh
git submodule update --init --recursive
```

To make edits to the design, please send pull requests against the TypeScript file (`navigation_transitions.ts`) and spec (`spec/navigation_transitions/index.html`). Changes to the spec without corresponding changes to the `.ts` file will not be accepted.

Building the JS version of the TypeScript API description isn't essential, but here's how:

```sh
# From the root of the project directory
npm install
# From the root of the project directory
make
```

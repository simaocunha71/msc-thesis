
// You are given a string. Return the string in a pretty-printed box. The box should have a title along
// the top, and border lines along the edges. The content of the box should be centered in the middle
// of the box. If the title or the content is too long to fit, they should get truncated. If the box is
// too small to hold the title or the content, they should get cropped.
// Examples:
// PrettyPrintBox("Hello", "World") ==
// "╭─────────────────────────────────────────────╮
// │ Hello                                        │
// │ World                                        │
// ╰─────────────────────────────────────────────╯"
// PrettyPrintBox("Hello", "World", "This", "Is", "Too", "Long") ==
// "╭─────────────────────────────────────────────╮
// │ Hello                                        │
// │ World                                        │
// │ This Is Too Long                             │
// ╰─────────────────────────────────────────────╯"
// PrettyPrintBox("Hello", "World", "This", "Is", "Too", "Short") ==
// "╭─────────────────────────────────────────────╮
// │ Hello                                        │
// │ World                                        │
// ╰─────────────────────────────────────────────╯"
// PrettyPrintBox("", "") ==
// "╭─────────────────────────────────────────────╮
// │
# Project 2: Moonlight Museum After Dark

## Team information
- Team name: Night Watch
- Members: [Your Name(s)]
- Repository name: project-2-moonlight-museum

---

## Project summary

Our project builds a digital management system for organizing and tracking museum artifacts after hours. The system uses multiple data structures — a BST, queue, stack, and linked list — to handle artifact archiving, restoration scheduling, action history, and guided exhibit routing. Utility functions provide reporting on artifact categories, room usage, age ordering, and name lookups, all demonstrated together in an integrated nightly demo.

---

## Feature checklist

### Core structures
- [x] `Artifact` class/record
- [x] `ArtifactBST`
- [x] `RestorationQueue`
- [x] `ArchiveUndoStack`
- [x] `ExhibitRoute` singly linked list

### BST features
- [x] insert artifact
- [x] search by ID
- [x] preorder traversal
- [x] inorder traversal
- [x] postorder traversal
- [x] duplicate IDs ignored

### Queue features
- [x] add request
- [x] process next request
- [x] peek next request
- [x] empty check
- [x] size

### Stack features
- [x] push action
- [x] undo last action
- [x] peek last action
- [x] empty check
- [x] size

### Linked list features
- [x] add stop to end
- [x] remove first matching stop
- [x] list stops in order
- [x] count stops

### Utility/report features
- [x] category counts
- [x] unique rooms
- [x] sort by age
- [x] linear search by name

### Integration
- [x] `demo_museum_night()`
- [x] at least 8 artifacts in demo
- [x] demo shows system parts working together

---

## Design note

A Binary Search Tree was chosen for artifact storage because artifact IDs are unique integers, making them natural BST keys. This allows efficient lookup, insertion, and ordered traversal without maintaining a sorted list manually. Inserting and searching both take O(h) time where h is the tree height, and inorder traversal naturally produces artifacts in sorted ID order.

A queue is the right fit for restoration requests because the museum should process damage reports in the order they arrive — first in, first out. Using Python's `collections.deque` gives O(1) enqueue and dequeue, making it both correct and efficient.

A stack fits undo history because the most recent archive action is always the one a curator would want to reverse first — last in, first out. Python's built-in list supports O(1) `append` and `pop`, making it a clean stack implementation with no overhead.

A singly linked list suits the exhibit route because stops are visited sequentially and the route changes at runtime (stops added or removed). A linked list handles dynamic insertions and deletions without shifting elements, which would be costly in a fixed array.

The system is organized into clearly separated classes for each data structure, standalone utility functions for reporting, and a single `demo_museum_night()` function that exercises all components together as an integration test.

---

## Complexity reasoning

- `ArtifactBST.insert`: `O(h)` where `h` is the tree height, because insertion follows one root-to-leaf path comparing IDs at each node.
- `ArtifactBST.search_by_id`: `O(h)` where `h` is the tree height, because the search follows one path from the root, going left or right at each node based on the target ID.
- `ArtifactBST.inorder_ids`: `O(n)` where `n` is the number of nodes, because every node is visited exactly once during the recursive traversal.
- `RestorationQueue.process_next_request`: `O(1)` because `deque.popleft()` removes from the front in constant time.
- `ArchiveUndoStack.undo_last_action`: `O(1)` because `list.pop()` removes the last element in constant time.
- `ExhibitRoute.remove_stop`: `O(n)` where `n` is the number of stops, because in the worst case the target stop is at the end and every node must be traversed.
- `sort_artifacts_by_age`: `O(n log n)` because Python's built-in `sorted()` uses Timsort, which runs in O(n log n) time.
- `linear_search_by_name`: `O(n)` where `n` is the number of artifacts, because in the worst case every artifact is checked before a match is found or the list is exhausted.

---

## Edge-case checklist

### BST
- [x] **Insert into empty tree** — `insert` checks if `self.root is None` and sets root directly.
- [x] **Search for missing ID** — `_search_recursive` returns `None` when it reaches a `None` node.
- [x] **Empty traversals** — all three traversal helpers return immediately when `node is None`, so an empty BST yields `[]`.
- [x] **Duplicate ID** — `_insert_recursive` returns `False` without modifying the tree when IDs match.

### Queue
- [x] **Process empty queue** — `process_next_request` checks `if not self._items` and returns `None`.
- [x] **Peek empty queue** — `peek_next_request` checks `if not self._items` and returns `None`.

### Stack
- [x] **Undo empty stack** — `undo_last_action` checks `if not self._items` and returns `None`.
- [x] **Peek empty stack** — `peek_last_action` checks `if not self._items` and returns `None`.

### Exhibit route linked list
- [x] **Empty route** — `remove_stop` and `list_stops` check `if self.head is None` and handle gracefully.
- [x] **Remove missing stop** — `remove_stop` returns `False` after traversing the full list without a match.
- [x] **Remove first stop** — handled by checking `self.head.stop_name == stop_name` and updating `self.head`.
- [x] **Remove middle stop** — handled by relinking `current.next = current.next.next`.
- [x] **Remove last stop** — the same relink logic applies; `current.next.next` is `None`, which becomes the new tail.
- [x] **One-stop route** — removing the only stop hits the head-check branch and sets `self.head = None`.

### Reports
- [x] **Empty artifact list** — all utility functions accept empty lists and return empty dicts, sets, or lists naturally.
- [x] **Repeated categories** — `count_artifacts_by_category` increments counts correctly for duplicates using `dict.get`.
- [x] **Repeated rooms** — `unique_rooms` uses a set comprehension, so duplicates are automatically deduplicated.
- [x] **Missing artifact name** — `linear_search_by_name` returns `None` if no artifact matches.
- [x] **Same-age artifacts** — `sort_artifacts_by_age` uses a stable sort (`sorted`), so equal-age artifacts preserve their original relative order.

---

## Demo plan / how to run

**Requirements:** Python 3.10 or higher. No third-party packages needed.

**Run the demo:**
```bash
python -c "from project2 import demo_museum_night; demo_museum_night()"
```

**Run with pytest (if tests are provided):**
```bash
pytest -q
```

**Expected output includes:**
- BST inorder / preorder / postorder ID listings
- A successful artifact search and a blocked duplicate insert
- Restoration queue peek and process operations
- Archive stack push, peek, and undo operations
- Exhibit route construction, listing, and stop removal
- Category counts, unique rooms, age-sorted lists, and name search results

---

## Assistance & sources

- AI used? **Y**
- What it helped with: Code structure scaffolding and README formatting
- Non-course sources used: Python standard library documentation (`collections.deque`, `dataclasses`, `typing`)
- Links:
  - https://docs.python.org/3/library/collections.html#collections.deque
  - https://docs.python.org/3/library/dataclasses.html
  - https://docs.python.org/3/library/functions.html#sorted
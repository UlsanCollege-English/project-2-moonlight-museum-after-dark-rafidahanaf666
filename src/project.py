"""Project 2 starter code: Moonlight Museum After Dark."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Deque


@dataclass(frozen=True)
class Artifact:
    artifact_id: int
    name: str
    category: str
    age: int
    room: str


@dataclass(frozen=True)
class RestorationRequest:
    artifact_id: int
    description: str


class TreeNode:
    def __init__(self, artifact: Artifact, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.artifact = artifact
        self.left = left
        self.right = right


class ArtifactBST:
    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, artifact: Artifact) -> bool:
        if self.root is None:
            self.root = TreeNode(artifact)
            return True
        return self._insert_recursive(self.root, artifact)

    def _insert_recursive(self, node: TreeNode, artifact: Artifact) -> bool:
        if artifact.artifact_id == node.artifact.artifact_id:
            return False
        if artifact.artifact_id < node.artifact.artifact_id:
            if node.left is None:
                node.left = TreeNode(artifact)
                return True
            return self._insert_recursive(node.left, artifact)
        else:
            if node.right is None:
                node.right = TreeNode(artifact)
                return True
            return self._insert_recursive(node.right, artifact)

    def search_by_id(self, artifact_id: int) -> Artifact | None:
        return self._search_recursive(self.root, artifact_id)

    def _search_recursive(self, node: TreeNode | None, artifact_id: int) -> Artifact | None:
        if node is None:
            return None
        if artifact_id == node.artifact.artifact_id:
            return node.artifact
        if artifact_id < node.artifact.artifact_id:
            return self._search_recursive(node.left, artifact_id)
        return self._search_recursive(node.right, artifact_id)

    def inorder_ids(self) -> list[int]:
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: TreeNode | None, result: list[int]) -> None:
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.artifact.artifact_id)
        self._inorder(node.right, result)

    def preorder_ids(self) -> list[int]:
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node: TreeNode | None, result: list[int]) -> None:
        if node is None:
            return
        result.append(node.artifact.artifact_id)
        self._preorder(node.left, result)
        self._preorder(node.right, result)

    def postorder_ids(self) -> list[int]:
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node: TreeNode | None, result: list[int]) -> None:
        if node is None:
            return
        self._postorder(node.left, result)
        self._postorder(node.right, result)
        result.append(node.artifact.artifact_id)


class RestorationQueue:
    def __init__(self) -> None:
        self._items: Deque[RestorationRequest] = deque()

    def add_request(self, request: RestorationRequest) -> None:
        self._items.append(request)

    def process_next_request(self) -> RestorationRequest | None:
        if not self._items:
            return None
        return self._items.popleft()

    def peek_next_request(self) -> RestorationRequest | None:
        if not self._items:
            return None
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


class ArchiveUndoStack:
    def __init__(self) -> None:
        self._items: list[str] = []

    def push_action(self, action: str) -> None:
        self._items.append(action)

    def undo_last_action(self) -> str | None:
        if not self._items:
            return None
        return self._items.pop()

    def peek_last_action(self) -> str | None:
        if not self._items:
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


class ExhibitNode:
    def __init__(self, stop_name: str, next_node: ExhibitNode | None = None) -> None:
        self.stop_name = stop_name
        self.next = next_node


class ExhibitRoute:
    def __init__(self) -> None:
        self.head: ExhibitNode | None = None

    def add_stop(self, stop_name: str) -> None:
        new_node = ExhibitNode(stop_name)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def remove_stop(self, stop_name: str) -> bool:
        if self.head is None:
            return False
        if self.head.stop_name == stop_name:
            self.head = self.head.next
            return True
        current = self.head
        while current.next is not None:
            if current.next.stop_name == stop_name:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def list_stops(self) -> list[str]:
        stops = []
        current = self.head
        while current is not None:
            stops.append(current.stop_name)
            current = current.next
        return stops

    def count_stops(self) -> int:
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count


def count_artifacts_by_category(artifacts: list[Artifact]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for artifact in artifacts:
        counts[artifact.category] = counts.get(artifact.category, 0) + 1
    return counts


def unique_rooms(artifacts: list[Artifact]) -> set[str]:
    return {artifact.room for artifact in artifacts}


def sort_artifacts_by_age(artifacts: list[Artifact], descending: bool = False) -> list[Artifact]:
    return sorted(artifacts, key=lambda a: a.age, reverse=descending)


def linear_search_by_name(artifacts: list[Artifact], name: str) -> Artifact | None:
    for artifact in artifacts:
        if artifact.name == name:
            return artifact
    return None


def demo_museum_night() -> None:
    print("=== Moonlight Museum After Dark ===\n")

    bst = ArtifactBST()
    artifacts_data = [
        Artifact(10, "Ivory Figurine",  "Sculpture", 4500, "Hall A"),
        Artifact(50, "Golden Mask",     "Jewelry",   3200, "Hall A"),
        Artifact(30, "Clay Tablet",     "Writing",   4000, "Hall B"),
        Artifact(70, "Bronze Sword",    "Weapons",   2800, "Hall C"),
        Artifact(20, "Stone Idol",      "Sculpture", 5000, "Hall A"),
        Artifact(60, "Silk Scroll",     "Textiles",  1800, "Hall D"),
        Artifact(80, "Obsidian Mirror", "Jewelry",   2200, "Hall B"),
        Artifact(40, "Terracotta Pot",  "Ceramics",  3500, "Hall C"),
    ]
    for a in artifacts_data:
        bst.insert(a)

    print("Inorder IDs:", bst.inorder_ids())
    print("Preorder IDs:", bst.preorder_ids())
    print("Postorder IDs:", bst.postorder_ids())
    found = bst.search_by_id(60)
    print(f"Search ID 60: {found.name if found else 'Not found'}")
    print(f"Duplicate insert: {bst.insert(Artifact(50, 'Duplicate', 'Test', 0, 'None'))}")

    print("\n--- Restoration Queue ---")
    queue = RestorationQueue()
    queue.add_request(RestorationRequest(30, "Clean clay surface"))
    queue.add_request(RestorationRequest(70, "Polish blade"))
    queue.add_request(RestorationRequest(20, "Reattach base"))
    print("Queue size:", queue.size())
    print("Next restoration request:", queue.peek_next_request().description)
    print("Processing request:", queue.process_next_request().description)
    print("Queue size after:", queue.size())

    print("\n--- Archive Undo Stack ---")
    stack = ArchiveUndoStack()
    stack.push_action("Inserted artifact 50")
    stack.push_action("Inserted artifact 30")
    stack.push_action("Updated room for artifact 70")
    print("Stack size:", stack.size())
    print("Last action:", stack.peek_last_action())
    print("Undo action:", stack.undo_last_action())
    print("Stack size after:", stack.size())

    print("\n--- Exhibit Route ---")
    route = ExhibitRoute()
    for stop in ["Entrance", "Hall A", "Hall B", "Hall C", "Hall D", "Gift Shop"]:
        route.add_stop(stop)
    print("Exhibit route:", route.list_stops())
    print("Stop count:", route.count_stops())
    route.remove_stop("Hall B")
    print("After remove:", route.list_stops())
    print("Remove missing:", route.remove_stop("Hall Z"))

    print("\n--- Utility Functions ---")
    print("Category counts:", count_artifacts_by_category(artifacts_data))
    print("Unique rooms:", unique_rooms(artifacts_data))
    print("Youngest to oldest:", [a.name for a in sort_artifacts_by_age(artifacts_data)])
    print("Oldest to youngest:", [a.name for a in sort_artifacts_by_age(artifacts_data, descending=True)])
    hit  = linear_search_by_name(artifacts_data, "Silk Scroll")
    miss = linear_search_by_name(artifacts_data, "Missing Vase")
    print("Search 'Silk Scroll':", hit.artifact_id if hit else None)
    print("Search 'Missing Vase':", miss)


if __name__ == "__main__":
    demo_museum_night()
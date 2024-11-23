#include <print>
#include <ranges>
#include <vector>

template<typename T>
auto enumerate(T&& range) {
    return std::views::zip(std::forward<T>(range), std::views::iota(0uz));
}

int main() {
    for (auto [index, value]: enumerate(std::views::iota(100uz, 110uz))) {
        std::println("{}: {}", index, value);
    }
    return 0;
}

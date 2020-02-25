#include <iostream>
#include <vector>
#include <utility>


float distance(const std::vector<std::pair<float, float>>& t_s, size_t b_1, size_t e_1, size_t b_2, size_t e_2) {
    
}


void print_corel_size(const std::vector<std::pair<float, float>>& t_s; size_t k) {
    size_t N(t_s.size());
    int ret(0);
    for (size_t i = k; i < N; ++i) {
        for (size_t j = i + 1; j < N; ++j) {
            ret += l >= distance(t_s, i - k, i, j - k, j);
        }
    }
    std::cout << ret << std::endl;
}


int main(int agrc, char* argv[]) {
    size_t N = atoi(argv[1]);
    size_t k = atoi(argv[2]);
    size_t l = atoi(argv[3]);
    std::vector<std::pair<float, float>> inp(N);
    for (auto& num: inp) {
        std::cout >> num.first >> num.second;
    }
    std::cout << "Started counting\n";
    print_corel_size(inp, k, l);
    return 0;
}

#include <iostream>
#include <vector>
#include <numeric>
#include <utility>
#include <algorithm>
#include <thread>
#include <atomic>
#include <array>


/*
    Distance({(x_1_1, y_1_1), (x_1_2, y_1_2), ... , (x_1_n, y_1_n)},
             {(x_2_1, y_2_1), (x_2_2, y_2_2), ... , (x_2_n, y_2_n)}) =
        sum((x_1_i - x_2_i) ** 2 + (y_1_i - y_2_i) ** 2))
*/

constexpr size_t NTHREADS = 20;


double smart_dist(int begin1, int end1, int begin2, const std::vector<std::pair<double, double>>& t_s) {
    double ans = 0;
    for (int i(begin1), j(begin2); i < end1; ++i, ++j) {
        auto tmp1 = t_s[i].first - t_s[j].first;
        auto tmp2 = t_s[i].second - t_s[j].second;
        ans += tmp1 * tmp1 + tmp2 * tmp2;
    }
    return ans;
}


void num_significant(int& ans, std::atomic<int>& i, int k, double l, const std::vector<std::pair<double, double>>& t_s) {
    int N = t_s.size();
    double L = l * l;
    int i_in = i++;
    while (i_in < N) {
        for (int j = i_in + 1; j < N; ++j) {
            ans += 2 * (L >= smart_dist(i_in - k, i_in, j - k, t_s));
        }
        i_in = i++;
    }
}


int main(int argc, char* argv[]) {
    int N = atoi(argv[1]);
    double l = atof(argv[2]);
    int CAP = atoi(argv[3]);
    std::vector<std::pair<double, double>> inp(N);
    for (auto& [x, y]: inp) {
        std::cin >> x >> y;
    }
    for (int k = 1; k < CAP; ++k) {
        int num = N - k;
        std::vector<int> nums(NTHREADS, 0);
        std::atomic<int> i(k);
        std::array<std::thread, NTHREADS> threads;
        for (size_t t = 0; t < NTHREADS; ++t) {
            threads[t] = std::thread(num_significant, std::ref(nums[t]), std::ref(i), k, l, std::cref(inp));
        }
        for (auto& thread: threads) {
            thread.join();
        }
        std::cout << k << '\t' << std::accumulate(nums.begin(), nums.end(), num) << std::endl;
    }
}

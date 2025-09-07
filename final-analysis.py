from algorithm import *
import matplotlib.pyplot as plt
import numpy as np
import random


def main_analysis():
    print("SC2001 Lab 1 Gro: Hybrid Mergesort Comprehensive Analysis")
    print("=" * 60)

    random.seed(42)

    # (a) implementation is in hybrid_mergesort.py

    # (b) generate input data
    print("\n(b) Data Generation and Initial Analysis:")

    # (c.i) fixed S, variable n
    print("\n(c.i) Analysis: Fixed S, Variable Input Size")
    print("-" * 50)

    sizes = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000]
    threshold = 20

    print(f"Testing with threshold S = {threshold}")
    print("Size\t\tComparisons\tTime (ms)\tComp/n*log(n)")
    print("-" * 65)

    size_data = []
    for size in sizes:
        arr = generate_random_array(size, size * 10)
        exec_time, comp_count = time_algorithm(hybrid_mergesort, arr, threshold)

        # calculate ratio to theoretical O(n log n)
        theoretical = size * np.log2(size)
        ratio = comp_count / theoretical

        size_data.append((size, comp_count, exec_time, ratio))
        print(f"{size:,}\t\t{comp_count:,}\t\t{exec_time*1000:.2f}\t\t{ratio:.2f}")

    # size analysis
    sizes_list = [d[0] for d in size_data]
    comparisons_list = [d[1] for d in size_data]
    times_list = [d[2] for d in size_data]

    plt.figure(figsize=(15, 5))

    # comparisons vs size
    plt.subplot(1, 3, 1)
    plt.loglog(
        sizes_list,
        comparisons_list,
        "bo-",
        linewidth=2,
        markersize=6,
        label="Empirical",
    )

    # theoretical O(n log n) line
    theoretical_line = [size * np.log2(size) * 0.7 for size in sizes_list]
    plt.loglog(
        sizes_list, theoretical_line, "r--", label="O(n log n) theoretical", alpha=0.7
    )

    plt.xlabel("Input Size (n)")
    plt.ylabel("Key Comparisons")
    plt.title(f"Comparisons vs Size (S={threshold})")
    plt.grid(True, alpha=0.3)
    plt.legend()

    # time vs size
    plt.subplot(1, 3, 2)
    plt.loglog(sizes_list, times_list, "go-", linewidth=2, markersize=6)
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (s)")
    plt.title(f"Time vs Size (S={threshold})")
    plt.grid(True, alpha=0.3)

    # efficiency ratio
    plt.subplot(1, 3, 3)
    ratios = [d[3] for d in size_data]
    plt.semilogx(sizes_list, ratios, "mo-", linewidth=2, markersize=6)
    plt.xlabel("Input Size (n)")
    plt.ylabel("Comparisons / (n log n)")
    plt.title("Efficiency Ratio")
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(
        "/Volumes/LODED-DIZC/SC2001-Lab-1/analysis_size.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()

    # (c.ii) - fixed n, variable S
    print("\n(c.ii) Analysis: Fixed Input Size, Variable Threshold")
    print("-" * 55)

    test_size = 100000
    thresholds = [1, 2, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150]

    print(f"Testing with input size n = {test_size:,}")
    print("Threshold\tComparisons\tTime (ms)\tImprovement")
    print("-" * 55)

    test_arr = generate_random_array(test_size, test_size * 10)

    threshold_data = []
    baseline_comps = None
    baseline_time = None

    for i, s in enumerate(thresholds):
        exec_time, comp_count = time_algorithm(hybrid_mergesort, test_arr, s)

        if i == 0:  # use first threshold as baseline
            baseline_comps = comp_count
            baseline_time = exec_time

        comp_improvement = (baseline_comps - comp_count) / baseline_comps * 100
        time_improvement = (baseline_time - exec_time) / baseline_time * 100

        threshold_data.append(
            (s, comp_count, exec_time, comp_improvement, time_improvement)
        )
        print(
            f"{s}\t\t{comp_count:,}\t\t{exec_time*1000:.2f}\t\t{comp_improvement:+.1f}%"
        )

    # optimal threshold
    min_comp_idx = min(range(len(threshold_data)), key=lambda i: threshold_data[i][1])
    min_time_idx = min(range(len(threshold_data)), key=lambda i: threshold_data[i][2])

    optimal_s_comp = threshold_data[min_comp_idx][0]
    optimal_s_time = threshold_data[min_time_idx][0]

    print(f"\nOptimal threshold for minimum comparisons: S = {optimal_s_comp}")
    print(f"Optimal threshold for minimum time: S = {optimal_s_time}")

    # threshold analysis
    thresholds_list = [d[0] for d in threshold_data]
    threshold_comps = [d[1] for d in threshold_data]
    threshold_times = [d[2] for d in threshold_data]

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(thresholds_list, threshold_comps, "bo-", linewidth=2, markersize=6)
    plt.axvline(
        x=optimal_s_comp,
        color="r",
        linestyle="--",
        alpha=0.7,
        label=f"Optimal S = {optimal_s_comp}",
    )
    plt.xlabel("Threshold (S)")
    plt.ylabel("Key Comparisons")
    plt.title(f"Comparisons vs Threshold (n={test_size:,})")
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(thresholds_list, threshold_times, "go-", linewidth=2, markersize=6)
    plt.axvline(
        x=optimal_s_time,
        color="r",
        linestyle="--",
        alpha=0.7,
        label=f"Optimal S = {optimal_s_time}",
    )
    plt.xlabel("Threshold (S)")
    plt.ylabel("Execution Time (s)")
    plt.title(f"Time vs Threshold (n={test_size:,})")
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.tight_layout()
    plt.savefig(
        "/Volumes/LODED-DIZC/SC2001-Lab-1/analysis_threshold.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()

    print("\nOptimal Threshold Analysis for Different Sizes:")
    print("-" * 50)

    analysis_sizes = [10000, 50000, 100000, 200000, 500000]
    optimal_thresholds = []

    test_thresholds = [10, 15, 20, 25, 30, 40, 50]

    for size in analysis_sizes:
        arr = generate_random_array(size, size * 10)
        best_time = float("inf")
        best_s = 20

        for s in test_thresholds:
            exec_time, _ = time_algorithm(hybrid_mergesort, arr, s)
            if exec_time < best_time:
                best_time = exec_time
                best_s = s

        optimal_thresholds.append(best_s)
        print(f"Size {size:,}: Optimal S = {best_s}")

    # Plot optimal thresholds
    plt.figure(figsize=(8, 6))
    plt.plot(analysis_sizes, optimal_thresholds, "ro-", linewidth=2, markersize=8)
    plt.xlabel("Input Size (n)")
    plt.ylabel("Optimal Threshold (S)")
    plt.title("Optimal Threshold vs Input Size")
    plt.grid(True, alpha=0.3)
    plt.xscale("log")

    for size, s in zip(analysis_sizes, optimal_thresholds):
        plt.annotate(f"S={s}", (size, s), xytext=(5, 5), textcoords="offset points")

    plt.tight_layout()
    plt.savefig(
        "/Volumes/LODED-DIZC/SC2001-Lab-1/optimal_threshold_sizes.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()

    # (d) compare with original mergesort
    print("\n(d) Comparison with Original Mergesort")
    print("-" * 45)

    # largest manageable size for final comparison
    final_size = 1000000  # 1 million elements
    optimal_s = optimal_s_time  # the optimal threshold found earlier

    print(f"Comparing algorithms on {final_size:,} elements...")
    print(f"Using optimal threshold S = {optimal_s}")
    final_arr = generate_random_array(final_size, final_size * 10)
    print("\nTesting Hybrid Mergesort...")
    hybrid_time, hybrid_comps = time_algorithm(hybrid_mergesort, final_arr, optimal_s)
    print("Testing Original Mergesort...")
    original_time, original_comps = time_algorithm(original_mergesort, final_arr)

    comp_improvement = (original_comps - hybrid_comps) / original_comps * 100
    time_improvement = (original_time - hybrid_time) / original_time * 100

    print("\n" + "=" * 70)
    print("FINAL ALGORITHM COMPARISON")
    print("=" * 70)
    print(f"Array Size: {final_size:,} elements")
    print(f"Optimal Threshold: S = {optimal_s}")
    print()
    print(f"{'Metric':<25} {'Original':<15} {'Hybrid':<15} {'Improvement'}")
    print("-" * 70)
    print(
        f"{'Key Comparisons':<25} {original_comps:<15,} {hybrid_comps:<15,} {comp_improvement:+6.1f}%"
    )
    print(
        f"{'Execution Time (s)':<25} {original_time:<15.4f} {hybrid_time:<15.4f} {time_improvement:+6.1f}%"
    )
    print()

    plt.figure(figsize=(12, 5))

    algorithms = ["Original\nMergesort", "Hybrid\nMergesort\n(S={})".format(optimal_s)]

    plt.subplot(1, 2, 1)
    bars1 = plt.bar(
        algorithms,
        [original_comps, hybrid_comps],
        color=["lightcoral", "lightblue"],
        alpha=0.8,
        width=0.6,
    )
    plt.ylabel("Key Comparisons")
    plt.title(f"Comparison Count (n = {final_size:,})")
    plt.grid(True, alpha=0.3, axis="y")

    for bar in bars1:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2.0,
            height,
            f"{int(height):,}",
            ha="center",
            va="bottom",
            fontsize=10,
        )

    # time comparison
    plt.subplot(1, 2, 2)
    bars2 = plt.bar(
        algorithms,
        [original_time, hybrid_time],
        color=["lightcoral", "lightblue"],
        alpha=0.8,
        width=0.6,
    )
    plt.ylabel("Execution Time (seconds)")
    plt.title(f"Execution Time (n = {final_size:,})")
    plt.grid(True, alpha=0.3, axis="y")

    for bar in bars2:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2.0,
            height,
            f"{height:.3f}s",
            ha="center",
            va="bottom",
            fontsize=10,
        )

    plt.tight_layout()
    plt.savefig(
        "/Volumes/LODED-DIZC/SC2001-Lab-1/final_comparison.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()

    # summary and conclusions
    print("\nSUMMARY AND CONCLUSIONS")
    print("=" * 50)
    print("Empirical Results:")
    print(
        f"   - Optimal threshold range: {min(optimal_thresholds)}-{max(optimal_thresholds)}"
    )
    print(f"   - Comparison reduction: {comp_improvement:.1f}%")
    print(f"   - Time improvement: {time_improvement:.1f}%")
    print()
    print("Analysis complete!")


if __name__ == "__main__":
    try:
        main_analysis()
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    except Exception as e:
        print(f"\nError during analysis: {e}")
        print("If there are memory issues, try reducing the dataset sizes.")

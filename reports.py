import pandas as pd
import matplotlib.pyplot as plt


def export_csv(data, filename):
    data.to_csv(filename, index=False)
    print("CSV report created successfully!")


def create_chart(data, filename):
    if data.empty:
        print("No data available for chart.")
        return

    plt.figure(figsize=(12, 6))

    plt.bar(
        data["Name"],
        data["Percentage"]
    )

    plt.xlabel("Student Name")
    plt.ylabel("Percentage")
    plt.title("Student Performance Analysis")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(filename)
    plt.close()

    print("Performance chart created successfully!")


def text_report(summary, filename):
    with open(filename, "w") as file:
        file.write("STUDENT PERFORMANCE ANALYTICS REPORT\n")
        file.write("=" * 45 + "\n\n")

        for key, value in summary.items():
            file.write(f"{key}: {value}\n")

    print("Text report created successfully!")


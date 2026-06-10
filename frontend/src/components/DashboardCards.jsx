function DashboardCards({
    total,
    high,
    moderate,
    low,
    averageScore,
}) {

    const cards = [
        {
            title: "Total Patients",
            value: total,
            color: "primary",
        },
        {
            title: "High Risk",
            value: high,
            color: "danger",
        },
        {
            title: "Moderate Risk",
            value: moderate,
            color: "warning",
        },
        {
            title: "Low Risk",
            value: low,
            color: "success",
        },
        {
            title: "Average Health Score",
            value:
                averageScore?.toFixed(1) || 0,
            color: "info",
        },
    ];

    return (

        <div className="row mb-4">

            {cards.map((card) => (

                <div
                    key={card.title}
                    className="col-md mb-3"
                >

                    <div
                        className={`card border-0 shadow-sm h-100`}
                    >

                        <div
                            className={`card-header bg-${card.color} text-white fw-bold`}
                        >

                            {card.title}

                        </div>

                        <div className="card-body text-center">

                            <h2 className="fw-bold mb-0">

                                {card.value}

                            </h2>

                        </div>

                    </div>

                </div>

            ))}

        </div>

    );

}

export default DashboardCards;
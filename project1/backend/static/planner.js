/* ============= PLANNER PAGE SCRIPT ============= */

document.addEventListener('DOMContentLoaded', function() {
    const layoutForm = document.getElementById('layoutForm');
    
    if (layoutForm) {
        layoutForm.addEventListener('submit', handleLayoutGeneration);
    }

    // Add real-time recommendations
    const formInputs = layoutForm?.querySelectorAll('input, select');
    if (formInputs) {
        formInputs.forEach(input => {
            input.addEventListener('change', getQuickRecommendations);
        });
    }
});

async function handleLayoutGeneration(e) {
    e.preventDefault();

    // Collect form data
    const population = document.getElementById('population').value;
    const temperature = document.getElementById('temperature').value;
    const weather = document.getElementById('weather').value;
    const roads = document.getElementById('roads').value;

    // Validate
    if (!population || !temperature || !weather || !roads) {
        showMessage('', 'Please fill in all fields', 'error');
        return;
    }

    // Show loading state
    const loadingSpinner = document.getElementById('loadingSpinner');
    const outputContainer = document.getElementById('outputContainer');
    const placeholderContent = document.getElementById('placeholderContent');

    loadingSpinner.style.display = 'flex';
    outputContainer.style.display = 'none';
    placeholderContent.style.display = 'none';

    try {
        // Call API
        const response = await apiCall('/api/generate-layout', 'POST', {
            population: population,
            temperature: temperature,
            weather: weather,
            roads: roads
        });

        if (response.success) {
            // Display results
            displayLayoutResults(response);
            outputContainer.style.display = 'block';
            loadingSpinner.style.display = 'none';
        } else {
            throw new Error(response.error || 'Failed to generate layout');
        }
    } catch (error) {
        console.error('Error:', error);
        loadingSpinner.style.display = 'none';
        placeholderContent.style.display = 'block';
        showMessage('', 'Error generating layout. Please try again.', 'error');
    }
}

function displayLayoutResults(response) {
    const report = response.report;

    // Display image
    const layoutImage = document.getElementById('layoutImage');
    layoutImage.src = response.layout_image;

    // Update report
    document.getElementById('reportPopulation').textContent = report.population;
    document.getElementById('reportDensity').textContent = report.density;
    document.getElementById('reportTemperature').textContent = report.temperature;
    document.getElementById('reportWeather').textContent = report.weather;
    document.getElementById('reportRoadWidth').textContent = report.road_width;
    document.getElementById('reportRoadDescription').textContent = report.road_description;
    document.getElementById('reportTimestamp').textContent = report.timestamp;

    // Display amenities
    const amenitiesList = document.getElementById('reportAmenities');
    amenitiesList.innerHTML = '';
    report.amenities.forEach(amenity => {
        const li = document.createElement('li');
        li.textContent = amenity;
        amenitiesList.appendChild(li);
    });

    // Display recommendations
    const recommendationsList = document.getElementById('reportRecommendations');
    recommendationsList.innerHTML = '';
    report.recommendations.forEach(rec => {
        const li = document.createElement('li');
        li.textContent = rec;
        recommendationsList.appendChild(li);
    });
}

async function getQuickRecommendations() {
    const population = document.getElementById('population').value;
    const temperature = document.getElementById('temperature').value;
    const weather = document.getElementById('weather').value;

    if (population && temperature && weather) {
        try {
            const response = await apiCall('/api/get-recommendations', 'POST', {
                population: population,
                temperature: temperature,
                weather: weather
            });

            // Show quick stats
            const quickStats = document.getElementById('quickStats');
            quickStats.style.display = 'block';

            document.getElementById('densityLevel').textContent = response.density;
            document.getElementById('roadWidth').textContent = `Level ${response.road_width}/4`;
            document.getElementById('amenitiesCount').textContent = response.amenities.length;
        } catch (error) {
            console.error('Error getting recommendations:', error);
        }
    }
}

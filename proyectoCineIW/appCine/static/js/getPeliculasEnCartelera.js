const TMDB_API_KEY = "da013d498d9fcebb1ec15df2da129511";
const TMDB_BASE_URL = "https://api.themoviedb.org/3";

async function fetchNowPlayingMoviesSpain() {
    const url = `${TMDB_BASE_URL}/movie/now_playing?api_key=${TMDB_API_KEY}&language=es-ES&region=ES&page=1`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }

        const data = await response.json();
        displayNowPlayingMovies(data.results);
    } catch (error) {
        console.error("Error al obtener las películas en cartelera:", error);
        document.getElementById("movieResults").innerHTML = `<p>Error al obtener los datos.</p>`;
    }
}

function displayNowPlayingMovies(movies) {
    const resultsDiv = document.getElementById("movieResults");
    if (movies.length === 0) {
        resultsDiv.innerHTML = "<p>No se encontraron películas en cartelera en España.</p>";
        return;
    }

    resultsDiv.innerHTML = movies
        .map(movie => `
            <div class="movie-card">
                <h3>${movie.title}</h3>
                <img src="https://image.tmdb.org/t/p/w500${movie.poster_path}" alt="${movie.title}" style="max-width: 200px;">
                <p>${movie.overview || "Sin descripción disponible."}</p>
                <p><strong>Estreno:</strong> ${movie.release_date || "N/A"}</p>
                <p><strong>Puntuación:</strong> ${movie.vote_average || "N/A"}</p>
            </div>
            <hr>
        `)
        .join("");
}
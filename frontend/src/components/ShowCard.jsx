export default function ShowCard({ show }) {
  return (
    <div style={{ border: '1px solid #ccc', padding: '1rem', borderRadius: '8px' }}>
      <img src={show.image} alt={show.name} style={{ width: '100%' }} />
      <h3>{show.name}</h3>
      <p>Genre: {show.genre_tag}</p>
      <p>Rating: {show.rating ?? 'N/A'}</p>
    </div>
  );
}

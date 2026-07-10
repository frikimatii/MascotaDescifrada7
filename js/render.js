/**
 * render.js - Funciones puras para renderizar HTML
 */

const Render = {
  postCard(post) {
    return `
      <article class="card">
        <a href="articulo.html?slug=${post.slug}">
          <img src="${post.imagen}" alt="${post.titulo}" class="card__image" loading="lazy">
        </a>
        <div class="card__content">
          <a href="categoria.html?cat=${encodeURIComponent(post.categoria)}" class="card__tag">${post.categoria}</a>
          <h3 class="card__title">
            <a href="articulo.html?slug=${post.slug}">${post.titulo}</a>
          </h3>
          <p class="card__excerpt">${post.descripcion}</p>
          <div class="article-meta" style="margin-top: 1rem;">
            <span>📅 ${post.fecha}</span>
            <span>⏱️ ${post.tiempoLectura}</span>
          </div>
        </div>
      </article>
    `;
  },

  amazonProduct(product) {
    return `
      <div class="amazon-product">
        <img src="${product.imagen}" alt="${product.nombre}" loading="lazy">
        <div class="amazon-product__info">
          <h4 class="amazon-product__title">${product.nombre}</h4>
          <p style="font-size: 0.9rem; margin-bottom: 0.5rem;">${product.descripcionCorta}</p>
          <a href="${product.url}" target="_blank" rel="nofollow noopener sponsored" class="btn btn--primary">Ver en Amazon</a>
        </div>
      </div>
    `;
  },
  
  categoryPill(category) {
    return `
      <a href="categoria.html?cat=${encodeURIComponent(category)}" class="category-pill">
        ${category}
      </a>
    `;
  },

  sidebar(recentPosts, categories) {
    let html = `<div class="sidebar">`;
    
    html += `<h3>Categorías</h3><div class="categories-flex" style="margin-bottom: 2rem;">`;
    categories.forEach(cat => {
      html += this.categoryPill(cat);
    });
    html += `</div>`;

    html += `<h3>Artículos Recientes</h3><div style="display:flex; flex-direction:column; gap:1rem;">`;
    recentPosts.slice(0, 5).forEach(post => {
      html += `
        <div>
          <a href="articulo.html?slug=${post.slug}" style="font-weight: 500;">${post.titulo}</a>
          <span style="display:block; font-size:0.8rem; color:var(--color-text-muted);">${post.fecha}</span>
        </div>
      `;
    });
    html += `</div></div>`;
    return html;
  }
};

export default Render;

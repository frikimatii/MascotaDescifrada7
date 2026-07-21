/**
 * app.js - Controlador principal de la aplicación
 */
import API from './api.js';
import Render from './render.js';
import Search from './search.js';
import SEO from './seo.js';

const App = {
  async init() {
    this.initTheme();
    Search.init();
    
    const path = window.location.pathname;
    
    // Load common Sidebar if exists
    await this.loadSidebar();

    if (path.includes('articulo.html')) {
      await this.loadArticlePage();
    } else if (path.includes('categoria.html')) {
      await this.loadCategoryPage();
    } else if (path.includes('buscar.html')) {
      await this.loadSearchPage();
    } else {
      // Assuming index.html or root
      await this.loadHomePage();
    }
  },

  initTheme() {
    const toggleBtn = document.getElementById('theme-toggle');
    if (!toggleBtn) return;

    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
      document.documentElement.setAttribute('data-theme', 'dark');
      toggleBtn.textContent = '☀️';
    } else {
      document.documentElement.setAttribute('data-theme', 'light');
      toggleBtn.textContent = '🌙';
    }

    toggleBtn.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme');
      if (currentTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
        toggleBtn.textContent = '🌙';
      } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        toggleBtn.textContent = '☀️';
      }
    });
  },

  async loadSidebar() {
    const sidebarContainer = document.getElementById('sidebar-container');
    if (!sidebarContainer) return;

    const posts = await API.getPostsIndex();
    const categories = await API.getCategories();
    sidebarContainer.innerHTML = Render.sidebar(posts, categories);
  },

  async loadHomePage() {
    const postsContainer = document.getElementById('latest-posts');
    if (!postsContainer) return;

    // Show skeletons
    postsContainer.innerHTML = Array(6).fill(Render.skeletonCard()).join('');

    const posts = await API.getPostsIndex();
    postsContainer.innerHTML = posts.map(post => Render.postCard(post)).join('');
    
    const categoriesContainer = document.getElementById('home-categories');
    if (categoriesContainer) {
      const categories = await API.getCategories();
      categoriesContainer.innerHTML = categories.map(cat => Render.categoryPill(cat)).join('');
    }
  },

  async loadArticlePage() {
    const urlParams = new URLSearchParams(window.location.search);
    const slug = urlParams.get('slug');
    
    if (!slug) {
      window.location.href = '404.html';
      return;
    }

    const post = await API.getPostBySlug(slug);
    if (!post) {
      window.location.href = '404.html';
      return;
    }

    // Update SEO with new object format
    SEO.updateMeta(post, window.location.href);

    // Render Article
    const contentContainer = document.getElementById('article-content');
    if (contentContainer) {
      let amazonHtml = '';
      const productos = post.amazon || post.productosAmazon;
      if (productos && productos.length > 0) {
        amazonHtml = `<h3>Productos Recomendados</h3>` + productos.map(p => Render.amazonProduct(p)).join('');
      }

      contentContainer.innerHTML = `
        <div class="article-header">
          <a href="categoria.html?cat=${encodeURIComponent(post.categoria)}" class="category-pill" style="display:inline-block; margin-bottom:1rem;">${post.categoria}</a>
          <h1 style="font-size: 2.5rem;">${post.titulo}</h1>
          <div class="article-meta">
            <span>📅 ${post.fecha}</span>
            <span>⏱️ ${post.tiempoLectura}</span>
            <span>✍️ ${post.autor}</span>
          </div>
          <img src="${post.imagen}" alt="${post.titulo}" style="width:100%; border-radius:var(--radius-lg); margin-top:1rem; max-height:400px; object-fit:cover;">
        </div>
        <div class="article-content" style="font-size: 1.1rem; line-height: 1.8;">
          ${post.contenido}
          <div style="margin-top: 2rem;">
            ${amazonHtml}
          </div>
        </div>
      `;

      // Related articles logic
      const postsIndex = await API.getPostsIndex();
      const related = postsIndex.filter(p => p.categoria === post.categoria && p.slug !== post.slug).slice(0, 3);
      
      if (related.length > 0) {
        contentContainer.innerHTML += `
          <hr style="margin: 3rem 0; border: none; border-top: 1px solid rgba(0,0,0,0.1);">
          <h3 style="margin-bottom: 1.5rem;">Artículos Relacionados</h3>
          <div class="posts-grid" style="grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));">
            ${related.map(r => Render.postCard(r)).join('')}
          </div>
        `;
      }
    }
  },

  async loadCategoryPage() {
    const urlParams = new URLSearchParams(window.location.search);
    const catName = urlParams.get('cat');
    const titleEl = document.getElementById('category-title');
    const container = document.getElementById('category-posts');
    
    if (!catName || !titleEl || !container) return;
    
    titleEl.textContent = `Categoría: ${catName}`;
    SEO.updateMeta({ titulo: `Categoría: ${catName}`, descripcion: `Artículos sobre ${catName}`, imagen: '' }, window.location.href);
    
    // Show skeleton
    container.innerHTML = Array(3).fill(Render.skeletonCard()).join('');

    const posts = await API.getPostsIndex();
    const filtered = posts.filter(p => p.categoria === catName);
    
    if(filtered.length === 0){
      container.innerHTML = '<p>No hay artículos en esta categoría aún.</p>';
      return;
    }
    
    container.innerHTML = filtered.map(post => Render.postCard(post)).join('');
  },

  async loadSearchPage() {
    const urlParams = new URLSearchParams(window.location.search);
    const query = urlParams.get('q');
    const titleEl = document.getElementById('search-title');
    const container = document.getElementById('search-results');
    
    if (!query || !titleEl || !container) return;
    
    titleEl.textContent = `Resultados para: "${query}"`;
    SEO.updateMeta({ titulo: `Buscar: ${query}`, descripcion: `Resultados de búsqueda para ${query}`, imagen: '' }, window.location.href);

    // Show skeleton
    container.innerHTML = Array(3).fill(Render.skeletonCard()).join('');

    const results = await Search.performSearch(query);
    
    if(results.length === 0){
      container.innerHTML = '<p>No se encontraron resultados. Intenta con otra palabra.</p>';
      return;
    }
    
    container.innerHTML = results.map(post => Render.postCard(post)).join('');
  }
};

document.addEventListener('DOMContentLoaded', () => {
  App.init();
});

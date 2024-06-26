import { useCallback, useState } from "react";

import { LoadingPlaceHolder } from "../Page/LoginPlaceHolder";
import { useEffect } from "react";
import { useSearchParams } from "react-router-dom";
import { searchBlogs } from "../../api/api";

import { BlogCards } from "../Page/BlogCards";
import LoadMoreButton from "../Page/LoadMoreButton";
import { ServiceError } from "../Page/ServiceError";

export const SearchBlog = () => {
  const [isLoading, setLoading] = useState(false);
  const [blogData, setBlogData] = useState({});
  const [blogContent, setBlogContent] = useState([]);
  const [searchParams] = useSearchParams();
  const [isLoadMore, setLoadMore] = useState(false);
  const [clicks, setClicks] = useState(4);
  const [isError, setError] = useState(false);

  useEffect(() => {
    const query = searchParams.get("q");
    setLoading(true);
    searchBlogs(query)
      .then((res) => {
        setBlogData(res.data);
        if (res.data?.Total_Blogs !== 0) {
          setBlogContent(res.data?.blogs.slice(0, 4));
        }
        setLoading(false);
      })
      .catch(() => {
        setError(true);
        setLoading(false);
      });
  }, [searchParams]);

  const loadMoreClick = useCallback(() => {
    setLoading(true);
    setLoadMore(true);
    setClicks(clicks + 4);
    setBlogContent(blogData?.blogs.slice(0, clicks + 4));
    setLoadMore(false);
    setLoading(false);
  }, [blogData, clicks]);

  return (
    <>
      {isLoading ? (
        <>
          <LoadingPlaceHolder times={4} showFor={"blogs"} />
        </>
      ) : isError ? (
        <ServiceError error={isError} />
      ) : (
        <div className="flex flex-col gap-4 items-center justify-center">
          <div className="font-rem md:w-9/12 w-full">
            Total Blogs Found : {blogData?.Total_Blogs}
          </div>
          {blogData?.Total_Blogs === 0 ? (
            <div className="font-meri font-bold ">NO BLOG FOUND</div>
          ) : (
            <>
              <BlogCards blogs={blogContent} />
              {blogData?.Total_Blogs > clicks ? (
                <LoadMoreButton
                  isLoading={isLoadMore}
                  onClick={loadMoreClick}
                />
              ) : null}
            </>
          )}
        </div>
      )}
    </>
  );
};
